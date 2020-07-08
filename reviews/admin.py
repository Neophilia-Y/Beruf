from django.contrib import admin
from . import models


@admin.register(models.Review, models.Comment)
class AdminReview(admin.ModelAdmin):
    """Admin review , comment """

    pass

