# 10-minute AISYS Demo Script

1. **Introduction (30s):** “This is a modular RFID-enabled library extension designed to integrate safely with an existing ILMS. I deliberately use adapter boundaries and synthetic data because the assignment excludes production access and physical hardware.”
2. **Architecture (60s):** Show the seven-layer design and explain why adapters isolate vendor/device dependencies.
3. **AC01 (60s):** Run the sample spreadsheet migration and show valid, rejected and duplicate counts.
4. **AC02 (45s):** Read an RFID tag and show its book relationship.
5. **AC03/04 (90s):** Checkout/renew/check-in and show reference/fine/block restrictions plus audit history.
6. **AC05 (45s):** Explain that repeated reader events form the basis of shelf inventory and missing/misplaced comparison.
7. **AC06/07 (75s):** Trigger gate event, show CCTV reference and queued notification; authenticate a mock staff smart card.
8. **AC08 (45s):** Show dashboard/reports/audit.
9. **AC09/10 (60s):** Explain offline installer/update/rollback and backup/restore runbooks.
10. **Close (30s):** “The prototype demonstrates the required boundaries and acceptance scenarios while keeping production data and vendor dependencies isolated. The remaining production work is vendor-specific integration, hardware validation and institutional deployment approval.”
