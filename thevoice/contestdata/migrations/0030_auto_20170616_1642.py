# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-16 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestdata', '0029_team_average_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='average_score',
            field=models.FloatField(default=0),
        ),
    ]