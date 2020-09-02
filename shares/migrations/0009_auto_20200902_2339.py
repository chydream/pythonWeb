# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-09-02 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0008_auto_20200902_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shares',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('d6003ddd-0a0f-4b55-955d-e718db7ae093'), verbose_name='股票ID'),
        ),
        migrations.AlterField(
            model_name='sharesdetail',
            name='close',
            field=models.FloatField(max_length=128, verbose_name='收盘价'),
        ),
        migrations.AlterField(
            model_name='sharesdetail',
            name='open',
            field=models.FloatField(max_length=128, verbose_name='开盘价'),
        ),
        migrations.AlterField(
            model_name='sharesdetail',
            name='pctChg',
            field=models.FloatField(default=0, verbose_name='涨跌幅'),
        ),
        migrations.AlterField(
            model_name='sharesdetail',
            name='peTTM',
            field=models.FloatField(default=0, verbose_name='滚动市盈率'),
        ),
        migrations.AlterField(
            model_name='sharesdetail',
            name='turn',
            field=models.FloatField(default=0, verbose_name='换手率'),
        ),
        migrations.AlterField(
            model_name='sharesdetail',
            name='volume',
            field=models.FloatField(default=0, verbose_name='成交量'),
        ),
    ]
