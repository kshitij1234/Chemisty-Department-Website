# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-18 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import research.models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0004_auto_20170709_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchareas',
            name='object_no',
            field=models.IntegerField(default=research.models.ResearchAreas.number),
        ),
    ]
