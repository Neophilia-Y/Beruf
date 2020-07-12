from django.views.generic import ListView
from . import models
from django.utils import timezone


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
