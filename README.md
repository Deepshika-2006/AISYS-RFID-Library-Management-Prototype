# AISYS RFID Library Management Prototype

Technical evaluation prototype aligned to the AISYS Software Development SOP. The solution uses a layered Django architecture and synthetic/mock integrations so it can be demonstrated without access to institutional production systems or physical RFID hardware.

## Stack
- Python 3.12+
- Django 5.2.7
- SQLite for zero-configuration local demonstration
- MySQL supported through environment configuration and PyMySQL
- HTML/CSS/JavaScript-free server-rendered UI (small CSS only)
- openpyxl for controlled spreadsheet migration

## Quick start on Windows
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```
Open http://127.0.0.1:8000/ and sign in with `aisys_admin` / `AISYS-Demo-2026`.

### MySQL
Create a database named `aisys_library`, then set in `.env`:
```
DB_ENGINE=mysql
DB_NAME=aisys_library
DB_USER=root
DB_PASSWORD=YOUR_PASSWORD
DB_HOST=127.0.0.1
DB_PORT=3306
```
Then run `python manage.py migrate` and `python manage.py seed_demo`.

## Acceptance scenario demo map
- AC01: `python manage.py import_library sample_data/library_records.xlsx` and Migration page
- AC02: RFID page → reader mock
- AC03: Circulation page → checkout/renew/check-in; audit log preserved
- AC04: mark a member blocked or a book reference-only and retry circulation
- AC05: RFID page → reader mock for shelf inventory proof-of-concept
- AC06: RFID page → security gate mock; creates event with mock CCTV reference and queued email flag
- AC07: RFID page → smart-card mock using `STAFF-001`
- AC08: Reports page and dashboard
- AC09: `deploy/offline_update.ps1` and `deploy/rollback.ps1` are demonstration runbooks
- AC10: `docs/backup_restore.md` explains backup/restore validation

## Architecture
User UI → Application services → RFID middleware adapters → NCIP/SIP2 interoperability boundaries → Data layer → Integration adapters → Operations.

## Important evaluation boundary
This is a candidate prototype. RFID hardware, live ILMS, real NCIP/SIP2 endpoints, CCTV, SMS, and email providers are intentionally mocked. No production credentials or personal data are included.
