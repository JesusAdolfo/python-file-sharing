# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='extension',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='location',
        ),
        migrations.AddField(
            model_name='upload',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
