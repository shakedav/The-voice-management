# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-15 18:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contestdata', '0021_activities_date_performed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activities',
            name='date_performed',
        ),
    ]