# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-09-03 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0013_auto_20200903_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shares',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('b7ca63c2-17d4-4e43-86be-a87cf2052b1c'), verbose_name='股票ID'),
        ),
    ]
