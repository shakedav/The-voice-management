# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-12 22:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contestdata', '0008_auto_20170613_0139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activities',
            name='average_score',
        ),
    ]
