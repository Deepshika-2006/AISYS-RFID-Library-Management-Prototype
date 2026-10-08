from django.contrib import admin
from .models import Member,Book,Circulation,AuditLog,RFIDEvent,MigrationRun
for m in [Member,Book,Circulation,AuditLog,RFIDEvent,MigrationRun]: admin.site.register(m)
