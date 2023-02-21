from django import forms 

class FbForm(forms.Form):
    name = forms.CharField(max_length=100)
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows':30,'cols':55,'style':'resize:none;'}))