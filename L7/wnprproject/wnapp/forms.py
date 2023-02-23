from django import forms
from .models import WnModel

CHOICES = [('Fuel','Fuel'),('petrol','Petrol'),('diesel','Diesel')]
class WnForm(forms.ModelForm):
    option = forms.ChoiceField(widget=forms.RadioSelect(choices=CHOICES),initial='Fuel')
    class Meta:
        model = WnModel
        fields = ['name','options']