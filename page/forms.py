from django import forms
from .models import Application

class CreateForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'age', 'introduce', 'image']
