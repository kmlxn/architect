# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vcard', '0014_project_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecttag',
            name='alias',
        ),
        migrations.AddField(
            model_name='projecttag',
            name='url_name',
            field=models.SlugField(default='some-url-name', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='url_name',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
