# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showtrip', '0010_auto_20170108_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waypoint',
            name='travel_path',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
