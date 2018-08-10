# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-15 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20161115_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='full_name',
            new_name='long_name',
        ),
        migrations.AddField(
            model_name='product',
            name='short_info',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]