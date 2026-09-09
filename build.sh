#!/bin/bash
set -e

# Install Python dependencies using break-system-packages flag
python3 -m pip install -r requirements.txt --break-system-packages

# Run database migrations and collect static files
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput --clear