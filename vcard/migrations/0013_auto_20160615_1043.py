# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vcard', '0012_project_url_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectpicture',
            old_name='picture',
            new_name='source',
        ),
    ]
