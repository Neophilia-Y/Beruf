from django.contrib import admin
from . import models


@admin.register(models.Review)
class AdminReview(admin.ModelAdmin):
    """Admin review """

    list_display = ("__str__", "rating_average")


@admin.register(models.Comment)
class AdminComment(admin.ModelAdmin):
    """Admin comment"""

    pass
