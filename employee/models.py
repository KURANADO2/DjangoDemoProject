from django.db import models

# Create your models here.


# 不再继承 ojbect 类，而是继承自 Django 框架的 models.Model 类
class Employee(models.Model):
    # AutoField 表示自增
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=200)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    amount = models.IntegerField()
    is_publish = models.BooleanField(default=False)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
