from django.contrib import admin
from . import models


@admin.register(models.List)
class AdminList(admin.ModelAdmin):

    list_display = (
        "name",
        "user",
        "product_count",
    )

    filter_horizontal = ("product",)
