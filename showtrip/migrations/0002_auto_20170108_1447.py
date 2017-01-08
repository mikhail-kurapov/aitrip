# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 14:47
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showtrip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='finished',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='published_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='started',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='jb',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
