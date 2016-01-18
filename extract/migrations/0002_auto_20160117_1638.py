# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extract', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metainfo',
            name='desc',
        ),
        migrations.AddField(
            model_name='metainfo',
            name='description',
            field=models.CharField(max_length=1000, blank=True),
        ),
    ]
