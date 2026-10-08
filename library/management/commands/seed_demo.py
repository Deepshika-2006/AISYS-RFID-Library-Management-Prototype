from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from library.models import Book,Member
class Command(BaseCommand):
 def handle(self,*a,**k):
  u,created=User.objects.get_or_create(username='aisys_admin');
  if created:u.set_password('AISYS-Demo-2026');u.is_staff=True;u.is_superuser=True;u.save()
  members=[('SYSTEM','System',''),('M001','Ananya Rao','ananya@example.test'),('M002','Rahul Kumar','rahul@example.test')]
  for c,n,e in members: Member.objects.get_or_create(card_no=c,defaults={'name':n,'email':e})
  books=[('BK001','978000000001','Python Fundamentals','A. Author','Programming','SHELF-A1',False,'RFID-0001'),('BK002','978000000002','Database Systems','B. Author','Database','SHELF-A2',False,'RFID-0002'),('BK003','978000000003','Reference Encyclopedia','C. Author','Reference','REF-01',True,'RFID-0003'),('BK004','978000000004','Networks','D. Author','Networks','SHELF-B1',False,'RFID-0004')]
  for a,isbn,t,au,cat,loc,ref,tag in books: Book.objects.get_or_create(accession_no=a,defaults={'isbn':isbn,'title':t,'author':au,'category':cat,'location':loc,'reference_only':ref,'rfid_tag':tag})
  self.stdout.write(self.style.SUCCESS('Synthetic demo data ready. Login: aisys_admin / AISYS-Demo-2026'))
