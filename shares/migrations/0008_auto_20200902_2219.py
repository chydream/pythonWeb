# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-09-02 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0007_auto_20200902_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharesDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='交易所行情日期')),
                ('code', models.CharField(max_length=32, unique=True, verbose_name='股票代码')),
                ('open', models.CharField(max_length=128, verbose_name='开盘价')),
                ('close', models.CharField(max_length=128, verbose_name='收盘价')),
                ('volume', models.IntegerField(default=0, verbose_name='成交量')),
                ('turn', models.SmallIntegerField(default=0, verbose_name='换手率')),
                ('pctChg', models.SmallIntegerField(default=0, verbose_name='涨跌幅')),
                ('peTTM', models.SmallIntegerField(default=0, verbose_name='滚动市盈率')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '股票详情',
                'verbose_name_plural': '股票详情',
                'db_table': 'shares_detail',
            },
        ),
        migrations.AlterField(
            model_name='shares',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('d0acfc0f-ae6a-4457-82fd-d39e659c1230'), verbose_name='股票ID'),
        ),
    ]
