# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showtrip', '0009_auto_20170108_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waypoint',
            name='travel_dest',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='waypoint',
            name='travel_mode',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='waypoint',
            name='travel_path',
            field=models.CharField(max_length=1000),
        ),
    ]
