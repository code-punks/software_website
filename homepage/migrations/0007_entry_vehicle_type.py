# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-09 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='vehicle_type',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
