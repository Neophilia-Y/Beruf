from django.contrib import admin
from . import models
from django.utils.html import mark_safe


@admin.register(models.Category, models.Condition)
class AdminItem(admin.ModelAdmin):
    """Handling Category, Condition Item admin"""

    pass


@admin.register(models.Photo)
class AdminPhoto(admin.ModelAdmin):
    """Photo Admin"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f"<img width=50px src='{obj.files.url}' />")

    get_thumbnail.short_description = "Thumbnail"


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Product)
class AdminProduct(admin.ModelAdmin):
    """Admin Product"""

    inlines = [
        PhotoInline,
    ]
    list_display = (
        "title",
        "price_format",
        "host",
        "category",
        "created",
        "count_condition",
        "count_photos",
    )

    list_filter = ("category", "host__id_checked")

    search_fields = ["title", "^host__username"]

    filter_horizontal = ("condition",)

    fieldsets = (
        ("Basic Info", {"fields": ("host", "title", "description")}),
        ("Detail Info", {"fields": ("price", "category", "condition")}),
    )

    raw_id_fields = ("host",)

    def count_condition(self, obj):
        return obj.condition.count()

    count_condition.short_description = "Condition"

    def count_photos(self, obj):
        return obj.photo_set.count()

    count_photos.short_description = "Photo"

    def price_format(self, obj):
        return f"{obj.price:,}"

    price_format.short_description = "price"
