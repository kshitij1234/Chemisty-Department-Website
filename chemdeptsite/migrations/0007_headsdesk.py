# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-12 08:04
from __future__ import unicode_literals

import chemdeptsite.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemdeptsite', '0006_remove_news_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeadsDesk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to=chemdeptsite.models.get_image_path)),
                ('message', models.TextField()),
                ('profile', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'HeadsDesk',
            },
        ),
    ]