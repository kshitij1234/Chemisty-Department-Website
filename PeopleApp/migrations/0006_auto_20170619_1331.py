# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PeopleApp', '0005_auto_20170619_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='email',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]