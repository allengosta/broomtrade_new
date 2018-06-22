from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
# Create your views here.


class HowToBuyView(TemplateView, CategoryListMixin):
    template_name = "howtobuy.html"