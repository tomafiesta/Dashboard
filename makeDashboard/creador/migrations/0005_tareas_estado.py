# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creador', '0004_auto_20170326_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='tareas',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
