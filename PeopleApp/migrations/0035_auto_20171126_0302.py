# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-25 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PeopleApp', '0034_faculty_personal_cv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='personal_cv',
        ),
        migrations.AddField(
            model_name='faculty',
            name='personal_cv_link',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
