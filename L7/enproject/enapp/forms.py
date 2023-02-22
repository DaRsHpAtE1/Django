from django import forms
from .models import EnModel

class EnForms(forms.ModelForm):
    class Meta:
        model = EnModel
        fields = ["name","phone","course"]