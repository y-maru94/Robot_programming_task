from django import forms

class MyForm(forms.Form):
    text = forms.CharField(max_length=30)
