# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-17 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestdata', '0032_auto_20170616_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='candidate_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
