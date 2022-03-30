from django import forms
from django.contrib.auth.models import User
from .models import Client
# from django.forms.fields import ChoiceField

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email','phone','message')
        