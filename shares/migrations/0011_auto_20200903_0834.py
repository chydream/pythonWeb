# Generated by Django 3.1.1 on 2020-09-03 00:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0010_auto_20200902_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shares',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('9efd167f-27ff-4006-a980-f2e698f0fc5e'), verbose_name='股票ID'),
        ),
    ]