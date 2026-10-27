#!/bin/sh
# Container entrypoint: check the config, migrate, then serve.
# Migrations run here so a deploy either brings the schema up to date or never starts.
# Run ONE instance during a deploy: two starting together would migrate at the same time.
set -eu

pk check-config
pk migrate
exec uvicorn pehchana.main:app --host 0.0.0.0 --port "${PORT:-8000}" --proxy-headers
