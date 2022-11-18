from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('home/', views.home, name="home"),

    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register_page, name='register'),

    path('home/create_container/', views.create_container, name="create_container"),
    path('home/manage_container/', views.manage_container, name="manage_container"),
]

"""
    path('create_container/', views.create_container, name="create_container"),
    path('read_container/<str:pk>', views.read_container, name="read_container"),
    path('update_container/<str:pk>', views.update_container, name="update_container"),
    path('delete_container/<str:pk>', views.delete_container, name="delete_container"),
"""