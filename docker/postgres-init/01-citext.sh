#!/bin/sh
set -eu

# Django's test database is cloned from template1, so install citext there
# before the test database is created.
psql --username "$POSTGRES_USER" --dbname template1 \
  --command 'CREATE EXTENSION IF NOT EXISTS citext;'
