# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-28 18:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0044_auto_20170326_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductKitModelProxy',
            fields=[
            ],
            options={
                'verbose_name': '\u041d\u0430\u0431\u043e\u0440',
                'proxy': True,
                'verbose_name_plural': '\u041d\u0430\u0431\u043e\u0440\u044b',
            },
            bases=('shop.product',),
        ),
        migrations.AddField(
            model_name='product',
            name='best_before_1',
            field=models.DateField(blank=True, help_text='\u0441\u0442\u0430\u0440\u0430\u044f \u043f\u0430\u0440\u0442\u0438\u044f', null=True, verbose_name='\u0413\u043e\u0434\u0435\u043d \u0434\u043e'),
        ),
        migrations.AddField(
            model_name='product',
            name='best_before_2',
            field=models.DateField(blank=True, help_text='\u043d\u043e\u0432\u0430\u044f \u043f\u0430\u0440\u0442\u0438\u044f', null=True, verbose_name='\u0413\u043e\u0434\u0435\u043d \u0434\u043e 2'),
        ),
        migrations.AlterField(
            model_name='productoffer',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retailcrm_offers', to='shop.Product'),
        ),
    ]
