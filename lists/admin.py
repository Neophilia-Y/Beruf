from django.contrib import admin
from . import models


@admin.register(models.List)
class AdminList(admin.ModelAdmin):
    pass
