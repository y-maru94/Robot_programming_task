from django.shortcuts import render
from .forms import MyForm


def form_test(request):
    form = MyForm()
    return render(request, 'test_char/form.html', {
        'form': form,
    })
