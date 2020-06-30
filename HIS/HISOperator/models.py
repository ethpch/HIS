from django.db import models

# Create your models here.


class User(models.Model):
    userid = models.IntegerField('用户ID', max_length=10, primary_key=True)
    username = models.CharField('用户名称', max_length=20, unique=True)
    password = models.CharField('用户密码', max_length=20)
    role = models.CharField('用户角色', max_length=20)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'