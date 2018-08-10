# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-15 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='productimage',
            name='descripton',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='section',
            name='slug',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='section',
            name='products',
            field=models.ManyToManyField(blank=True, to='shop.Product'),
        ),
    ]