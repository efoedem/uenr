#!/bin/bash
# Runs on every Vercel deploy: apply database migrations, then collect
# static assets so CSS/images are served correctly in production.
set -e
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput
