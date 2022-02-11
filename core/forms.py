from django import forms
from .models import Pescription

class PescriptionCreateForm(forms.ModelForm):
    class Meta:
        model= Pescription
        exclude = ('user',)