from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from manager.models import *


class TestView(TemplateView):
    template_name = "test_view.html"

    def get(self, request, *args, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)
