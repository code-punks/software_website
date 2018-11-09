# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-09 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='month',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='balance',
            name='payment_balance',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='month',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='monthly_amount',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount_paid',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_month',
            field=models.IntegerField(blank=True),
        ),
    ]
