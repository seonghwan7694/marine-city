from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Container, User
from django import forms


class ContainerForm(ModelForm):
    class Meta:
        model = Container
        fields = ['port', 'goods', 'goods_cnt']

    port = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'manage_port']

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Confirm Password'}))
    manage_port = forms.ChoiceField(widget=forms.Select(),
                                    choices=([('부산항', '부산항'), ('싱가포르항', '싱가포르항'), ('터키항', '터키항')]), initial='부산항',
                                    required=True)
