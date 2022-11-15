from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Port(models.Model):
    port_list = (('부산항', '부산항'), ('싱가포르항', '싱가포르항'), ('터키항', '터키항'))
    port = models.CharField(max_length=10, choices=port_list)

    def __str__(self):
        return self.port


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    manage_port = models.ForeignKey(Port, on_delete=models.CASCADE, null=True)


class Goods(models.Model):
    goods = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.goods

    class Meta:
        # verbose_name = 'Goods'
        verbose_name_plural = 'Goods'


class Container(models.Model):
    port = models.ForeignKey(Port, on_delete=models.CASCADE, null=True)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, null=True)
    goods_cnt = models.IntegerField(default=1, validators=[MaxValueValidator(20), MinValueValidator(1)])
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return '#' + str(self.id)
