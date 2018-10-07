#!/bin/bash
set -e

# Running DB migrations
cd $API_PATH && python3 manage.py db upgrade

exec "$@"
