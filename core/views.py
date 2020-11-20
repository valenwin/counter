from django.shortcuts import render
from django.views.generic import TemplateView


class BasicView(TemplateView):
    template_name = 'base.html'
