# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PeopleApp', '0010_auto_20170622_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='phdstudents',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='phdstudents',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]