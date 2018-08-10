# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-06 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0058_auto_20170605_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegrambotrecipient',
            name='authorized',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='contentimage',
            name='image',
            field=models.ImageField(help_text='\n    \u042d\u0442\u043e\u0442 URL \u043c\u043e\u0436\u043d\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0432 \u043b\u044e\u0431\u043e\u043c \u043c\u0435\u0441\u0442\u0435 \u0441\u0430\u0439\u0442\u0430.\n    <br>\u041d\u0435 \u0443\u0434\u0430\u043b\u044f\u0439 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u0431\u0435\u0437 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e\u0441\u0442\u0438 (\u043d\u0435 \u043f\u0440\u043e\u0432\u0435\u0440\u0438\u0432 \u043a\u043e\u043d\u0442\u0435\u043d\u0442).\n    <br><br>\u0417\u0430\u0433\u0440\u0443\u0436\u0430\u0439 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0440\u0430\u0437\u043c\u0435\u0440\u0430!\n    <br><br>\u0417\u0430\u0442\u0435\u043c, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0435 URL \u0434\u043b\u044f \u0440\u0435\u0441\u0430\u0439\u0437\u0430 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438:\n    <br>&nbsp;/media/resize/<\u0448\u0438\u0440\u0438\u043d\u0430>/<\u043e\u0441\u0442\u0430\u043b\u044c\u043d\u043e\u0435>.jpg\n    <br>&nbsp;/media/resize/<\u0448\u0438\u0440\u0438\u043d\u0430>x<\u0432\u044b\u0441\u043e\u0442\u0430>/<\u043e\u0441\u0442\u0430\u043b\u044c\u043d\u043e\u0435>.jpg\n    <br>&nbsp;/media/crop/<\u0448\u0438\u0440\u0438\u043d\u0430>/<\u043e\u0441\u0442\u0430\u043b\u044c\u043d\u043e\u0435>.jpg</li>\n    <br>&nbsp;/media/crop/<\u0448\u0438\u0440\u0438\u043d\u0430>x<\u0432\u044b\u0441\u043e\u0442\u0430>/<\u043e\u0441\u0442\u0430\u043b\u044c\u043d\u043e\u0435>.jpg\n    ', upload_to='content-img'),
        ),
    ]
