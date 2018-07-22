from django import forms
from django.contrib.admin import widgets
import os

CHOICE = {
    ('0', 'キュート'),
    ('1', 'クール'),
    ('2', 'パッション'),
}

form SampleForm(forms.Form):
    select = forms.ChoiceField(
        label='属性', widget=forms.RadioSelect, choices=CHOICE, initial=0)
