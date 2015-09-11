# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vcard', '0002_contactinfo_textonsite'),
    ]

    operations = [
        migrations.AddField(
            model_name='textonsite',
            name='name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
