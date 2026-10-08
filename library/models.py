from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    card_no=models.CharField(max_length=40, unique=True)
    name=models.CharField(max_length=120)
    email=models.EmailField(blank=True)
    blocked=models.BooleanField(default=False)
    fine_amount=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    role=models.CharField(max_length=30,default='MEMBER')
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'{self.card_no} - {self.name}'

class Book(models.Model):
    accession_no=models.CharField(max_length=50,unique=True)
    isbn=models.CharField(max_length=30,blank=True)
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=150,blank=True)
    category=models.CharField(max_length=100,blank=True)
    location=models.CharField(max_length=120,default='Main Shelf')
    reference_only=models.BooleanField(default=False)
    status=models.CharField(max_length=30,default='AVAILABLE')
    rfid_tag=models.CharField(max_length=80,blank=True,unique=True,null=True)
    def __str__(self): return f'{self.accession_no} - {self.title}'

class Circulation(models.Model):
    book=models.ForeignKey(Book,on_delete=models.PROTECT)
    member=models.ForeignKey(Member,on_delete=models.PROTECT)
    action=models.CharField(max_length=20,choices=[('CHECKOUT','CHECKOUT'),('RENEW','RENEW'),('CHECKIN','CHECKIN')])
    due_date=models.DateTimeField(null=True,blank=True)
    operator=models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    note=models.CharField(max_length=255,blank=True)

class AuditLog(models.Model):
    actor=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    action=models.CharField(max_length=80)
    entity=models.CharField(max_length=80,blank=True)
    entity_id=models.CharField(max_length=80,blank=True)
    details=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

class RFIDEvent(models.Model):
    event_type=models.CharField(max_length=40)
    tag_id=models.CharField(max_length=80,blank=True)
    accession_no=models.CharField(max_length=50,blank=True)
    payload=models.JSONField(default=dict)
    created_at=models.DateTimeField(auto_now_add=True)

class MigrationRun(models.Model):
    source_name=models.CharField(max_length=200)
    total_rows=models.IntegerField(default=0)
    valid_rows=models.IntegerField(default=0)
    duplicate_rows=models.IntegerField(default=0)
    rejected_rows=models.IntegerField(default=0)
    imported_rows=models.IntegerField(default=0)
    rolled_back=models.BooleanField(default=False)
    error_log=models.JSONField(default=list)
    created_at=models.DateTimeField(auto_now_add=True)
