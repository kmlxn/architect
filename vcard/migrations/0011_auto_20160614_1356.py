# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vcard', '0010_delete_textonsite'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPicture',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('picture', models.ImageField(upload_to='projects')),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='picture',
        ),
        migrations.AddField(
            model_name='projectpicture',
            name='project',
            field=models.ForeignKey(to='vcard.Project', related_name='pictures'),
        ),
    ]
