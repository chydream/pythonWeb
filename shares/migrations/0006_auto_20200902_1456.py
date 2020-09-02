# Generated by Django 3.1.1 on 2020-09-02 06:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0005_auto_20200902_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shares',
            name='code_name',
            field=models.CharField(max_length=32, verbose_name='股票名称'),
        ),
        migrations.AlterField(
            model_name='shares',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('59bfe4e0-96b9-42c3-bfbf-57faaec33089'), verbose_name='股票ID'),
        ),
    ]