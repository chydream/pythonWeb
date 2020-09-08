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


class SharesDetail(models.Model):
    date = models.DateTimeField('交易所行情日期', max_length=128)
    code = models.CharField('股票代码', max_length=32)
    open = models.FloatField('开盘价', max_length=128, default=0)
    high = models.FloatField('最高价', max_length=128, default=0)
    low = models.FloatField('最低价', max_length=128, default=0)
    close = models.FloatField('收盘价', max_length=128, default=0)
    volume = models.FloatField('成交量', max_length=128, default=0)
    turn = models.FloatField('换手率', max_length=128, default=0)
    pctChg = models.FloatField('涨跌幅', max_length=128, default=0)
    peTTM = models.FloatField('滚动市盈率', max_length=128, default=0)
    isST = models.SmallIntegerField('是否ST股', default=0)
    preclose = models.FloatField('前收盘价', max_length=128, default=0)
    amount = models.FloatField('成交量', default=0)
    adjustflag = models.SmallIntegerField('复权状态', default=3)  # 1：后复权， 2：前复权，3：不复权
    tradestatus = models.SmallIntegerField('交易状态', default=1)  # 1：正常交易 0：停牌
    pbMRQ = models.FloatField('市净率', max_length=128, default=0)
    psTTM = models.FloatField('滚动市销率', max_length=128, default=0)
    pcfNcfTTM = models.FloatField('滚动市现率', max_length=128, default=0)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now_add=True)

    class Meta:
        db_table = 'shares_detail'
        verbose_name = '股票详情'
        verbose_name_plural = '股票详情'
        ordering = ['-date']

    def __str__(self):
        return self.code

