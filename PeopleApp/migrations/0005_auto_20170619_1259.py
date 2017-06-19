# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PeopleApp', '0004_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='email',
            field=models.TextField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.TextField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]