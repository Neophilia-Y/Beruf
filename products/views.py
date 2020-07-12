from django.views.generic import ListView, DetailView
from . import models
from django.utils import timezone
from django.shortcuts import render


class HomeView(ListView):

    """Home View class"""

    model = models.Product
    context_object_name = "products"
    page_kwarg = "page"
    paginate_by = 10
    paginate_orphans = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class ProductDetail(DetailView):
    """Product DetailView class"""

    model = models.Product
