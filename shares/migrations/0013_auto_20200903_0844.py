# Generated by Django 3.1.1 on 2020-09-03 00:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0012_auto_20200903_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shares',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('dc6ff75f-f495-4e5c-8116-f84eec296238'), verbose_name='股票ID'),
        ),
        migrations.AlterField(
            model_name='sharesdetail',
            name='date',
            field=models.CharField(max_length=128, verbose_name='交易所行情日期'),
        ),
    ]