from __future__ import unicode_literals

from django.db import migrations
from django.conf.global_settings import LANGUAGES


def migrate_languages(apps, schema_editor):
    Language = apps.get_model('users', 'Language')
    for abbreviation, name in LANGUAGES:
        Language.objects.create(abbreviation=abbreviation, name=name)


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_languages),
    ]
