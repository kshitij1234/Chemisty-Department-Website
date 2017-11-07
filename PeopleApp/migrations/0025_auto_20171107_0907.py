# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-07 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0008_auto_20171107_0858'),
        ('PeopleApp', '0024_faculty_current_research'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faculty',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='current_research',
        ),
        migrations.AddField(
            model_name='faculty',
            name='current_research',
            field=models.ManyToManyField(to='research.CurrentResearch'),
        ),
    ]
