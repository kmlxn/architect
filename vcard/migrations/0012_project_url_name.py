# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vcard', '0011_auto_20160614_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url_name',
            field=models.CharField(default='some_unique_url', unique=True, max_length=255),
            preserve_default=False,
        ),
    ]
