# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-25 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PeopleApp', '0033_auto_20171113_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='personal_cv',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
