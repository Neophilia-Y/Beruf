from django.shortcuts import render
from . import models


products = models.Product.objects.all()


def all_products(request):
    return render(
        request, template_name="product/home.html", context={"products": products}
    )
