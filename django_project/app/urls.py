from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create_container/', views.create_container, name="create_container"),
    path('read_container/<str:pk>', views.read_container, name="read_container"),
    path('update_container/<str:pk>', views.update_container, name="update_container"),
    path('delete_container/<str:pk>', views.delete_container, name="delete_container"),
]