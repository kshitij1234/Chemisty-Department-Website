# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 07:19
from __future__ import unicode_literals

import PeopleApp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PeopleApp', '0007_batch_undergraduatestudents'),
    ]

    operations = [
        migrations.CreateModel(
            name='MscStudents',
            fields=[
                ('rollno', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=PeopleApp.models.get_image_path)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PeopleApp.Batch')),
            ],
        ),
        migrations.AlterField(
            model_name='undergraduatestudents',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]