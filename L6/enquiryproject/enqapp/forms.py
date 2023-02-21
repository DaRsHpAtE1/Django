from django import forms

class EnForm(forms.Form):
    name = forms.CharField()
    phone = forms.IntegerField()
    subject = forms.CharField()