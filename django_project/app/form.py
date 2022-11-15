from django.forms import ModelForm
from .models import Container


class ContainerForm(ModelForm):
    class Meta:
        model = Container
        fields = '__all__'
