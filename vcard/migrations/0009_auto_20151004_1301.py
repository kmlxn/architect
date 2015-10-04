# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vcard', '0008_projecttag_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttag',
            name='alias',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
