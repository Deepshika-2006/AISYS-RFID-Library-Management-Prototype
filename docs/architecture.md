# Architecture Package

## Context
The prototype acts as a safe extension around an existing ILMS. The production database is not connected. All external interfaces are represented by adapter contracts and synthetic mocks.

## Layers
1. **User layer:** dashboard, OPAC/search, circulation, reports, administration.
2. **Application layer:** cataloguing, members, circulation rules, audit, migration and reporting services.
3. **RFID middleware:** device-neutral reader, gate and smart-card adapters.
4. **Interoperability:** NCIP 2.0 mock boundary and SIP2 boundary represented by `NCIPMockAdapter`.
5. **Data layer:** transactional DB, RFID events, audit logs, migration runs.
6. **Integration layer:** notification/CCTV references represented by provider-neutral mock payloads.
7. **Operations:** configuration, health endpoint, migrations, backup/restore and offline update runbooks.

## Data integrity strategy
- Never connect candidate code directly to an institutional production DB.
- Take a backup before any production integration.
- Perform spreadsheet imports inside a transaction.
- Reject invalid and duplicate rows before commit.
- Record source/target reconciliation counts.
- Keep audit records for administrative/circulation events.

## Adapter strategy
Each physical or vendor-specific device is hidden behind a small adapter. A mock implements the same conceptual contract, so a vendor SDK can be introduced later without changing application workflows.
