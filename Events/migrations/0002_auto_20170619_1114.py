# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'verbose_name_plural': 'Events'},
        ),
        migrations.AddField(
            model_name='events',
            name='s_w',
            field=models.CharField(choices=[('SM', 'Seminar'), ('WS', 'Workshop')], default='SM', max_length=2),
        ),
    ]
