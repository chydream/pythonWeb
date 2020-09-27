from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField('用户名', max_length=64)
    password = models.CharField('密码', max_length=255)
    avatar = models.ImageField('用户头像', upload_to='avatar', null=True, blank=True)
    nickname = models.CharField('昵称', max_length=64, null=True, blank=True)
    integral = models.IntegerField('用户的积分', default=0)
    level = models.SmallIntegerField('用户级别', default=0)

    class Meta:
        db_table = 'accounts_user'
        verbose_name = '用户账户'
        verbose_name_plural = '用户账户'

    def __str__(self):
        return self.username