from django.contrib import admin
from . import models


@admin.register(models.Category, models.Condition)
class AdminItem(admin.ModelAdmin):
    """Handling Category, Condition Item admin"""

    pass


@admin.register(models.Photo)
class AdminPhoto(admin.ModelAdmin):
    """Photo Admin"""

    pass


@admin.register(models.Product)
class AdminProduct(admin.ModelAdmin):
    """Admin Product"""

    pass
