# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-26 11:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0042_auto_20170326_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productoffers',
            name='count',
        ),
    ]
