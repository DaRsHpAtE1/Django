from django import forms
from .models import FbModel

class FbForms(forms.ModelForm):
    class Meta:
        model = FbModel
        widgets = {
            'feedback': forms.Textarea(attrs={'rows': 15, 'cols': 60,'style':'resize:none;'}),
        }
        fields = ["name","feedback"]
        