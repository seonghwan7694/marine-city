from django.contrib import admin
from .models import Container, Port, Goods, User
# Register your models here.

admin.site.register(Container)
admin.site.register(Port)
admin.site.register(Goods)
admin.site.register(User)
