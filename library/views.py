import json
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count,Q
from django.http import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Book,Member,Circulation,AuditLog,RFIDEvent,MigrationRun
from .forms import BookForm,MemberForm
from .services import RFIDReaderAdapter,GateAdapter,SmartCardAdapter,checkout,checkin,renew,audit

@login_required
def dashboard(request):
    ctx={'books':Book.objects.count(),'members':Member.objects.count(),'issued':Book.objects.filter(status='ISSUED').count(),'events':RFIDEvent.objects.count(),'fines':sum(float(x.fine_amount) for x in Member.objects.all()),'recent':AuditLog.objects.order_by('-created_at')[:8]}
    return render(request,'library/dashboard.html',ctx)

def login_view(request):
    if request.user.is_authenticated:return redirect('/')
    if request.method=='POST':
        u=authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
        if u: login(request,u); return redirect('/')
        messages.error(request,'Invalid credentials')
    return render(request,'library/login.html')
@login_required
def logout_view(request): logout(request); return redirect('/login/')
@login_required
def books(request):
    q=request.GET.get('q','')
    if request.method=='POST':
        f=BookForm(request.POST)
        if f.is_valid(): obj=f.save(); audit(request.user,'CREATE_BOOK','Book',obj.id,obj.title); messages.success(request,'Book created'); return redirect('/books/')
    return render(request,'library/books.html',{'books':Book.objects.filter(Q(title__icontains=q)|Q(accession_no__icontains=q)|Q(rfid_tag__icontains=q)),'form':BookForm(),'q':q})
@login_required
def members(request):
    if request.method=='POST':
        f=MemberForm(request.POST)
        if f.is_valid(): obj=f.save(); audit(request.user,'CREATE_MEMBER','Member',obj.id,obj.name); messages.success(request,'Member created'); return redirect('/members/')
    return render(request,'library/members.html',{'members':Member.objects.all(),'form':MemberForm()})
@login_required
def circulation(request):
    if request.method=='POST':
        book=get_object_or_404(Book,id=request.POST['book_id']); member=get_object_or_404(Member,id=request.POST['member_id']); action=request.POST['action']
        try:
            if action=='CHECKOUT': checkout(book,member,request.user)
            elif action=='CHECKIN': checkin(book,request.user)
            elif action=='RENEW': renew(book,member,request.user)
            messages.success(request,f'{action} completed')
        except ValueError as e: messages.error(request,str(e))
    return render(request,'library/circulation.html',{'books':Book.objects.all(),'members':Member.objects.all(),'records':Circulation.objects.order_by('-created_at')[:30]})
@login_required
def rfid(request):
    result=None; event=None
    if request.method=='POST':
        mode=request.POST.get('mode'); tag=request.POST.get('tag_id','')
        if mode=='read': result=RFIDReaderAdapter().read(tag)
        elif mode=='gate':
            book=Book.objects.filter(rfid_tag=tag).first(); event=GateAdapter().emit_unauthorized(tag,book.accession_no if book else 'UNKNOWN'); audit(request.user,'GATE_EVENT','RFIDEvent',event.id,json.dumps(event.payload)); result=event.payload
        elif mode=='card': result=SmartCardAdapter().authenticate(tag)
    return render(request,'library/rfid.html',{'result':result,'events':RFIDEvent.objects.order_by('-created_at')[:20]})
@login_required
def migration(request):
    return render(request,'library/migration.html',{'runs':MigrationRun.objects.order_by('-created_at')[:20]})
@login_required
def reports(request):
    return render(request,'library/reports.html',{'by_status':Book.objects.values('status').annotate(n=Count('id')),'events':RFIDEvent.objects.order_by('-created_at')[:50],'audit':AuditLog.objects.order_by('-created_at')[:50]})
@login_required
def health(request):
    from django.db import connection
    try:
        with connection.cursor() as c: c.execute('SELECT 1')
        db='OK'
    except Exception as e: db='ERROR: '+str(e)
    return JsonResponse({'status':'healthy','database':db,'books':Book.objects.count(),'events':RFIDEvent.objects.count()})
@login_required
def run_scenario(request,scenario):
    # Safe demo endpoint: creates/uses synthetic data only.
    from django.core.management import call_command
    call_command('seed_demo')
    if scenario==1: return redirect('/migration/')
    if scenario==2: return redirect('/rfid/')
    if scenario in (3,4): return redirect('/circulation/')
    if scenario in (5,6,7): return redirect('/rfid/')
    return redirect('/reports/')
