from django import forms
from django.contrib.admin import widgets

class MyForm(forms.Form):
    text = forms.CharField(max_length=30, required=True, label='名前')


class VoteForm(forms.Form):
    choice = forms.ModelChoiceField(
        queryset=None,
        label='選択',
        widget=forms.RadioSelect(),
        empty_label=None,
        error_messages={
            'required': "You didn't select a choice.",
            'invalid_choice': "invalid choice.",
        },

    )

    def __init__(self, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = question.choice_set.all()


class HelloForm(forms.Form):
    Question = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
        ('e', 'E'),
        ('f', '分からない')
    )
    choice = forms.ChoiceField(
        label='選択',
        widget=forms.RadioSelect,
        choices=Question,
        required=True,
        initial=0
    )
