from django import forms

CHOICES = [("PHd","Phd"),("MS","MS"),("MBA","MBA")]
class WnForm(forms.Form):
    name = forms.CharField()
    options = forms.CharField(widget=forms.Select(choices=CHOICES))