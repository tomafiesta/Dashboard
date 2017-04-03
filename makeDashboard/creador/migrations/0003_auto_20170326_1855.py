# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creador', '0002_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='tareas2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='author',
        ),
        migrations.DeleteModel(
            name='tareas',
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
