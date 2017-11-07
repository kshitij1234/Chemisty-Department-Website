# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-07 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PeopleApp', '0025_auto_20171107_0907'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batch',
            options={'verbose_name_plural': 'Batch'},
        ),
        migrations.AlterModelOptions(
            name='designations',
            options={'verbose_name_plural': 'Designations'},
        ),
        migrations.AlterModelOptions(
            name='faculty',
            options={'ordering': ('name',), 'verbose_name_plural': 'Faculty'},
        ),
        migrations.AlterModelOptions(
            name='mscstudents',
            options={'verbose_name_plural': 'MscStudents'},
        ),
        migrations.AlterModelOptions(
            name='phdalumni',
            options={'verbose_name_plural': 'PhdAlumni'},
        ),
        migrations.AlterModelOptions(
            name='phdstudents',
            options={'verbose_name_plural': 'PhdStudents'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name_plural': 'Staff'},
        ),
        migrations.AlterModelOptions(
            name='undergraduatestudents',
            options={'verbose_name_plural': 'UndergraduateStudents'},
        ),
        migrations.AlterField(
            model_name='faculty',
            name='current_research',
            field=models.ManyToManyField(blank=True, to='research.CurrentResearch'),
        ),
    ]
