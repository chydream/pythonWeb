# Generated by Django 3.1.1 on 2020-09-27 17:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0022_auto_20200927_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shares',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('f238668d-2e4c-43b5-b2e7-5a269f1e178e'), verbose_name='股票ID'),
        ),
    ]