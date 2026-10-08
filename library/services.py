from datetime import timedelta
from django.utils import timezone
from .models import Book,Member,Circulation,AuditLog,RFIDEvent

class RFIDReaderAdapter:
    name='mock-reader'
    def read(self,tag_id):
        book=Book.objects.filter(rfid_tag=tag_id).first()
        return {'tag_id':tag_id,'accession_no':book.accession_no if book else None,'title':book.title if book else None,'found':bool(book)}

class GateAdapter:
    def emit_unauthorized(self,tag_id,accession_no,cctv_image='mock-cctv.jpg'):
        event=RFIDEvent.objects.create(event_type='UNAUTHORIZED_REMOVAL',tag_id=tag_id,accession_no=accession_no,payload={'cctv_image':cctv_image,'email_queued':True})
        return event

class SmartCardAdapter:
    def authenticate(self,card_no):
        return {'card_no':card_no,'authenticated':card_no.startswith('STAFF-'),'role':'LIBRARIAN' if card_no.startswith('STAFF-') else 'UNKNOWN'}

class NCIPMockAdapter:
    def checkout(self,book,member): return {'protocol':'NCIP 2.0','operation':'checkout','success':True,'book':book.accession_no,'member':member.card_no}
    def checkin(self,book): return {'protocol':'NCIP 2.0','operation':'checkin','success':True,'book':book.accession_no}
    def renew(self,book,member): return {'protocol':'SIP2/NCIP boundary','operation':'renew','success':True,'book':book.accession_no,'member':member.card_no}

def audit(actor,action,entity='',entity_id='',details=''):
    return AuditLog.objects.create(actor=actor,action=action,entity=entity,entity_id=str(entity_id),details=details)

def checkout(book,member,actor):
    if book.reference_only: raise ValueError('Reference item cannot circulate.')
    if member.blocked: raise ValueError('Member is blocked.')
    if member.fine_amount >= 100: raise ValueError('Member exceeds configurable fine limit.')
    if book.status != 'AVAILABLE': raise ValueError('Book is not available.')
    NCIPMockAdapter().checkout(book,member)
    book.status='ISSUED'; book.save(update_fields=['status'])
    due=timezone.now()+timedelta(days=14)
    Circulation.objects.create(book=book,member=member,action='CHECKOUT',due_date=due,operator=actor)
    audit(actor,'CHECKOUT','Book',book.id,f'member={member.card_no}')

def checkin(book,actor):
    NCIPMockAdapter().checkin(book)
    book.status='AVAILABLE'; book.save(update_fields=['status'])
    Circulation.objects.create(book=book,member=Member.objects.filter(card_no='SYSTEM').first() or Member.objects.first(),action='CHECKIN',operator=actor)
    audit(actor,'CHECKIN','Book',book.id,'book returned')

def renew(book,member,actor):
    NCIPMockAdapter().renew(book,member)
    due=timezone.now()+timedelta(days=14)
    Circulation.objects.create(book=book,member=member,action='RENEW',due_date=due,operator=actor)
    audit(actor,'RENEW','Book',book.id,f'member={member.card_no}')
