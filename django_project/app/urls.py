from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('home/', views.home, name="home"),

    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register_page, name='register'),

    path('home/create_container/', views.create_container, name="create_container"),
    path('home/detail_container/<str:pk>', views.detail_container, name="detail_container"),
    path('home/update_container/<str:pk>', views.update_container, name="update_container"),
    path('home/delete_container/<str:pk>', views.delete_container, name="delete_container"),
]