# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 16:10
from __future__ import unicode_literals

import creador.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creador', '0005_auto_20170416_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='inicioEjecucion',
            field=models.DateTimeField(default=creador.models.horainicio),
        ),
    ]
