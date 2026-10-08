# Requirements Traceability Matrix

| Requirement | Prototype evidence | Test/demo |
|---|---|---|
| FR01 Core ILMS | Books, members, circulation, reports | AC03/04/08 |
| FR02 Web/search | Books search and web UI | AC08 |
| FR03 RFID interoperability | RFIDReaderAdapter, GateAdapter, SmartCardAdapter, NCIPMockAdapter | AC02/03/05/06/07 |
| FR04 Circulation | Checkout, renew, check-in, reference/fine/block rules | AC03/04 |
| FR05 Tagging | RFID tag field and reader lookup | AC02 |
| FR06 Inventory | Device-neutral RFID read event model | AC05 |
| FR07 Security events | Gate event with accession + CCTV reference + notification flag | AC06 |
| FR08 Reports | Dashboard, audit and RFID reports | AC08 |
| FR09 Notifications | Provider-neutral queued notification flag in mock | AC06 |
| FR10 Migration | openpyxl importer with validation/duplicate/reconciliation stats | AC01 |
| FR11 Administration | Django admin, authentication, audit logs, health endpoint | AC07/08 |
| FR12 Offline lifecycle | Offline runbooks and update/rollback scripts | AC09 |
| NFR01 Data integrity | Transactional import, backup/restore procedure | AC01/10 |
| NFR02 Security | Django auth, CSRF, role boundary, secrets outside code | AC07 |
| NFR03 Compatibility | Windows setup and isolated deployment notes | AC09 |
| NFR04 Licensing | pinned requirements and license inventory | D4/D7 |
| NFR05 Testability | Django tests + acceptance test plan | D6 |
| NFR06 Maintainability | service/adapters separation, migrations, config | D2/D4 |
| NFR07 Supportability | `/health/`, audit logs, runbook | D8 |
| NFR08 Documentation | README, architecture, backup/restore, test docs | D8 |
