# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-17 19:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contestdata', '0033_auto_20170617_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activities',
            name='activity_score',
        ),
    ]
