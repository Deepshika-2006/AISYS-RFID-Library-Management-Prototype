from openpyxl import Workbook
wb=Workbook(); ws=wb.active; ws.title='Library'
headers=['accession_no','title','isbn','author','category','location','rfid_tag']; ws.append(headers)
rows=[('MIG001','Clean Code','978000111111','Robert Martin','Programming','MIG-A1','RFID-M001'),('MIG002','Operating Systems','978000222222','A. Silberschatz','Systems','MIG-A2','RFID-M002'),('MIG002','Duplicate Row','978000333333','Test','Test','MIG-A3','RFID-M003'),('','Invalid Missing Accession','978000444444','Test','Test','MIG-A4','RFID-M004'),('MIG003','Computer Networks','978000555555','Kurose','Networks','MIG-B1','RFID-M005')]
for r in rows: ws.append(r)
wb.save('library_records.xlsx')
