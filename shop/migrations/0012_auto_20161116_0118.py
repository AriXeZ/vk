# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-15 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_product_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='descripton',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]