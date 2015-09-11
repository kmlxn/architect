# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vcard', '0005_auto_20150907_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textonsite',
            name='text',
            field=models.TextField(),
        ),
    ]
