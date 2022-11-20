from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class User(AbstractUser):
    port_list = (('부산항', '부산항'), ('싱가포르항', '싱가포르항'), ('터키항', '터키항'))
    manage_port = models.CharField(max_length=10, choices=port_list)

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.manage_port


class Goods(models.Model):
    goods = models.CharField(max_length=20)
    goods_img = models.ImageField(default='/static/img/box2.png')

    def __str__(self):
        return self.goods


class Container(models.Model):
    port_list = (('부산항', '부산항'), ('싱가포르항', '싱가포르항'), ('터키항', '터키항'))
    port = models.CharField(max_length=10, choices=port_list)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    goods_cnt = models.IntegerField(default=1, validators=[MaxValueValidator(20), MinValueValidator(1)])
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['updated', 'created']

    def __str__(self):
        return '#' + str(self.id)
