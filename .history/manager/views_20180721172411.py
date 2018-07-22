from django.contrib.auth.views import login
from django.contrib.auth import authenticate
from django.views.generic import TemplateView

import csv

class CustomLoginView(TemplateView):
    template_name = "worker_list.html"
    f = open('data.csv', 'r')
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        print row
    f.close()

    def get(self, _, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect(self.get_next_redirect_url())
        else:
            kwargs = {'template_name': 'worker_list.html'}
            return login(self.request, *args, **kwargs)

    def post(self, _, *args, **kwargs):
        username = self.request.POST['username']
        user = authenticate(username=username, password=password)  # 1
        
        f = open('data.csv', 'w')
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(list)
        f.close()

        if user is not None:
            login(self.request, user)
            return redirect(self.get_next_redirect_url())
        else:
            kwargs = {'template_name': 'worker_list.html'}
            return login(self.request, *args, **kwargs)

    def get_next_redirect_url(self):
        redirect_url = self.request.GET.get('next')
        if not redirect_url or redirect_url == '/':
            redirect_url = '/worker_list/'
        return redirect_url
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic import TemplateView

# from manager.models import *
# import manager.form as forms
# from manager.forms import MyForm

# class WorkerListView(TemplateView):
#     template_name = "worker_list.html"
#     def form_test(request):
#         form = MyForm()
#         return render(request, 'worker_list/forms.html', {
#             'form': form,
#         })

    # def get(self, request, *args, **kwargs):
    #     form = forms.HelloForm(request.GET or None)
    #     # if form.is_valid():
    #     #     message = 'データ検証に成功しました'
    #     # else:
    #     #     message = 'データ検証に失敗しました'
    #     d = {
    #         'form': form,  # request.GET.get('your_name')#
    #         # 'message': message,
    #     }
    #     context = super(WorkerListView, self).get_context_data(**kwargs)
    #     return render(request, 'forms.html', d)
    #     #return render(self.request, self.template_name, context, d)
