from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from manager.models import *
import manager.form as forms

class WorkerListView(TemplateView):
    template_name = "worker_list.html"

    def get(self, request, *args, **kwargs):
        form = forms.HelloForm(request.GET or None)
        print form
        context = super(WorkerListView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)
