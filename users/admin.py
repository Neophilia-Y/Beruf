from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    """Custom Admin User"""

    list_display = (
        "username",
        "birthday",
        "id_checked",
        "address",
    )
    list_filter = ("id_checked",)

