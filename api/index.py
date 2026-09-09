"""Vercel serverless entry point for the Django app."""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uenr_portal.settings")

from django.core.wsgi import get_wsgi_application  # noqa: E402

app = get_wsgi_application()
application = app

# Vercel has no persistent build step for this runtime, so apply any pending
# database migrations once when the function boots.
if os.environ.get("RUN_MIGRATIONS", "true").lower() == "true":
    try:
        from django.core.management import call_command

        call_command("migrate", "--noinput")
    except Exception as exc:  # pragma: no cover - never block serving pages
        print(f"migrate skipped: {exc}")
