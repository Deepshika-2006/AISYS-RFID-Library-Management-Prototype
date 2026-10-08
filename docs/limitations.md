# Known limitations / production backlog

- Physical RFID readers, gates and smart cards are mocked.
- NCIP 2.0 and SIP2 are adapter boundaries, not claims of protocol certification.
- Email/SMS/CCTV are provider-neutral mocks.
- Search is database-backed prototype search; a production full-text index should be selected and benchmarked.
- Offline update scripts are runbook demonstrations, not a signed enterprise installer.
- Production deployment needs threat modeling, penetration testing, secrets management, backup policy approval, vendor SDK testing, performance testing with real 20,000+ records, and UAT.
