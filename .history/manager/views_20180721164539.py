from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from manager.models import *
import manager.form as forms

class WorkerListView(TemplateView):
    template_name = "worker_list.html"

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
