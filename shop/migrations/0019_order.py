# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-28 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20161127_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified_data', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('email_to_managers', models.BooleanField(default=False)),
                ('sync_to_frontpad', models.BooleanField(default=False)),
                ('email_to_customer', models.BooleanField(default=False)),
            ],
        ),
    ]