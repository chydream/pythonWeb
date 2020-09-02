import uuid

from django.db import models

# Create your models here.
class SharesCategory(models.Model):
    uid = models.UUIDField('分类ID', default=uuid.uuid4, editable=True)
    industry = models.CharField('所属行业', max_length=128, unique=True)
    industryClassification = models.CharField('所属行业类别', max_length=128)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now_add=True)
    count = models.IntegerField('数量', default=0)

    class Meta:
        db_table = 'shares_category'
        verbose_name = '股票分类'
        verbose_name_plural = '股票分类'
        ordering = ['-created_at']

    def __str__(self):
        return self.industry


class Shares(models.Model):
    uid = models.UUIDField('股票ID', default=uuid.uuid4(), editable=True)
    code = models.CharField('股票代码', max_length=32, unique=True)
    code_name = models.CharField('股票名称', max_length=32)
    # industry = models.ManyToOneRel(SharesCategory, to='industry', field_name='所属行业', related_name='industry')
    industry = models.CharField('所属行业', max_length=32, null=True, blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now_add=True)

    class Meta:
        db_table = 'shares'
        verbose_name = '股票'
        verbose_name_plural = '股票'
        ordering = ['-created_at']

    def __str__(self):
        return self.code_name