from django.views.generic import ListView, DetailView, View
from . import models
from . import forms
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


class SearchView(View):
    """Search view class"""

    def get(self, request):

        form = forms.searchForm(request.GET)

        if form.is_valid():
            title = form.cleaned_data.get("title")
            price = form.cleaned_data.get("price")
            category = form.cleaned_data.get("category")
            conditions = form.cleaned_data.get("condition")

            filter_args = {}

            if title:
                filter_args["title__contains"] = title
            if price:
                filter_args["price__lte"] = price
            if category:
                filter_args["category"] = category

            products = models.Product.objects.filter(**filter_args)

            if len(conditions) > 0:
                for condition in conditions:
                    products = products.filter(condition__pk=condition.pk)

            return render(
                request,
                template_name="products/search.html",
                context={"form": form, "products": products},
            )
        else:
            form = forms.searchForm()

        return render(
            request, template_name="products/search.html", context={"form": form}
        )

