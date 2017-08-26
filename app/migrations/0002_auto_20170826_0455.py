# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-26 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.IntegerField(unique=True),
        ),
    ]