# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-08-30 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharescategory',
            name='industry',
            field=models.CharField(max_length=128, unique=True, verbose_name='所属行业'),
        ),
    ]
