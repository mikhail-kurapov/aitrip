# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 10:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showtrip', '0020_auto_20170110_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waypoint',
            name='point',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='waypoint_point', to='showtrip.Point'),
        ),
    ]
