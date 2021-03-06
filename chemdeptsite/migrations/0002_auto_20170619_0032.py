# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemdeptsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='noticeboard',
            options={'verbose_name_plural': 'NoticeBoard'},
        ),
        migrations.AlterModelOptions(
            name='quicklinks',
            options={'verbose_name_plural': 'QuickLinks'},
        ),
        migrations.AlterModelOptions(
            name='research',
            options={'verbose_name_plural': 'Research'},
        ),
        migrations.AlterField(
            model_name='research',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
