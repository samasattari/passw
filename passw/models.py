from django.db import models

# Create your models here.
class Password (models.Model):
    title = models.CharField(max_length=50 ,verbose_name='عنوان')
    url = models.URLField(max_length=200 ,verbose_name='مسیر')
    password = models.CharField(max_length=225 ,verbose_name='رمز عبور')
    username = models.CharField(max_length=50,verbose_name='نام')
    description = models.TextField(max_length=200 ,blank=True ,null=True ,verbose_name='توضیحات')
