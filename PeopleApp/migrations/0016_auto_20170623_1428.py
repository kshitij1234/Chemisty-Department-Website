# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PeopleApp', '0015_phdalumni_thesis_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phdalumni',
            name='thesis_link',
            field=models.CharField(blank=True, default='#', max_length=200),
        ),
    ]
