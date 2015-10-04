# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vcard', '0007_auto_20151002_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttag',
            name='alias',
            field=models.CharField(max_length=255, default='fdsf'),
            preserve_default=False,
        ),
    ]
