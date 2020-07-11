from math import ceil
from django.shortcuts import render
from . import models


def all_products(request):
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 4
    limit = page_size * page
    offset = limit - page_size
    products = models.Product.objects.all()[offset:limit]
    page_count = ceil(models.Product.objects.count() / page_size)
    return render(
        request,
        template_name="product/home.html",
        context={"products": products, "page_count": page_count, "page": page},
    )
