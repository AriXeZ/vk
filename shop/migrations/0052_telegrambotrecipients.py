# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-29 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0051_auto_20170529_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramBotRecipients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_id', models.CharField(max_length=500, unique=True)),
            ],
        ),
    ]
