# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-15 18:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contestdata', '0023_activities_date_performed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='date_performed',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
