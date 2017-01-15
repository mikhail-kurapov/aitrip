# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showtrip', '0025_point_orderby'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='isfullinfo',
            field=models.CharField(blank=True, default=None, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='pointsbitmap',
            field=models.CharField(blank=True, default=None, max_length=16, null=True),
        ),
    ]
