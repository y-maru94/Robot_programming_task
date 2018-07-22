from django.shortcuts import render
import .forms

def form_test(request):
    form = MyForm()
    return render(request, 'polls/form.html', {
        'form': form,
    })
