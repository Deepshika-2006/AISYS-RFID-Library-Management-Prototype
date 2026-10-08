# Backup / Restore and AC10

For the candidate demo, use the database engine selected in `.env`.

## SQLite demo
Copy `db.sqlite3` to `backups/pre_change.sqlite3` before a risky migration. To restore, stop the server and replace `db.sqlite3` with the backup copy.

## MySQL
Use MySQL Workbench or `mysqldump` to create a pre-change dump. Example:
`mysqldump -u root -p aisys_library > backups/pre_change.sql`
Restore with:
`mysql -u root -p aisys_library < backups/pre_change.sql`

AC10 evidence should show: baseline record count → simulated failed change/import → restore → same baseline record count and sample records unchanged.
