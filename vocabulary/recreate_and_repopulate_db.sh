#!/bin/bash
DB_FILE="vocabulary.sqlite3"
DB_BACKUP_FILE="$DB_FILE.backup"

rm -f "$DB_BACKUP_FILE"
mv "$DB_FILE" "$DB_BACKUP_FILE"
sqlite3 "$DB_FILE" < schema.sql

./main.py "data/SATwords.xlsx" "$DB_FILE"
