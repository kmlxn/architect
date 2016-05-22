# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vcard', '0009_auto_20151004_1301'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TextOnSite',
        ),
    ]
