# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showtrip', '0023_auto_20170110_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trippoint',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='trip',
            name='thumbnail_new',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
