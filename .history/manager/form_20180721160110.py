# -*- coding: utf-8 -*-
from django import forms
from django.contrib.admin import widgets
import os

CHOICE = {
    ('0', 'キュート'),
    ('1', 'クール'),
    ('2', 'パッション'),
}

form SampleForm(forms.Form):
    file = open('./test.txt', 'w')
    #string = 'python output string'
    select = forms.ChoiceField(
        label='属性', widget=forms.RadioSelect, choices=CHOICE, initial=0)
    string = str(select)
    file.write(string)
