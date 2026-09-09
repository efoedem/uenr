import os
from django.db import migrations


def create_super_admin(apps, schema_editor):
    User = apps.get_model('auth', 'User')

    # Read credentials from environment variables or fall back to defaults
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'dues')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@uenr.edu.gh')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'Password1@$')

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )


class Migration(migrations.Migration):
    dependencies = [
        ('portal', '0001_initial'),  # Ensures this runs after your first migration
    ]

    operations = [
        migrations.RunPython(create_super_admin),
    ]