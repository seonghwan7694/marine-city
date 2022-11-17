from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Container, User


class ContainerForm(ModelForm):
    class Meta:
        model = Container
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'password1', 'password2']

class UserForm(ModelForm):
    class Meta:
        fields = ['avatar', 'name', 'username', 'manage_port']