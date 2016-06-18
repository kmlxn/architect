# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vcard', '0015_auto_20160618_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttag',
            name='url_name',
            field=models.SlugField(unique=True, max_length=255),
        ),
    ]
