# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-26 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20161125_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=models.ImageField(upload_to='product-previews'),
        ),
    ]
