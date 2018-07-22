from django.shortcuts import render


def form_test(request):
    form = MyForm()
    return render(request, 'polls/form.html', {
        'form': form,
    })
