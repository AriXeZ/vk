# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-16 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_product_preorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='overlay_image',
            field=models.ImageField(blank=True, upload_to=b'', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430 \u043f\u043e\u0432\u0435\u0440\u0445'),
        ),
    ]