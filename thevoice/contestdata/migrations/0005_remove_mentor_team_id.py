# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-12 21:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contestdata', '0004_activities_candidate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='team_id',
        ),
    ]
