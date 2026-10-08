# Test Package

| ID | Test | Expected result |
|---|---|---|
| T01 | RFID tag lookup | Known tag resolves to book |
| T02 | Checkout available book | Status becomes ISSUED and audit event is created |
| T03 | Reference book checkout | Operation rejected |
| T04 | Blocked member checkout | Operation rejected |
| T05 | Fine limit checkout | Operation rejected at configured threshold |
| T06 | Gate event | RFID event stores tag, accession and CCTV reference |
| T07 | Smart card | STAFF-* accepted as librarian mock |
| T08 | Migration duplicate | Duplicate counted and not imported |
| T09 | Migration invalid row | Invalid row rejected and logged |
| T10 | Health endpoint | Database and service health returned |

Run: `python manage.py test tests`
