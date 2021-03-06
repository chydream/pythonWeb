# Generated by Django 3.1.1 on 2020-09-08 03:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0019_auto_20200908_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shares',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('36142722-3d9a-47f4-b179-8297f94d5372'), verbose_name='股票ID'),
        ),
        migrations.AlterField(
            model_name='sharesdetail',
            name='date',
            field=models.DateTimeField(max_length=128, verbose_name='交易所行情日期'),
        ),
    ]
