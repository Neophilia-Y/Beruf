from django.contrib import admin
from . import models


@admin.register(models.Conversation)
class AdminConversation(admin.ModelAdmin):

    list_display = ("__str__", "count_message", "count_participants")


@admin.register(models.Message)
class AdminMessage(admin.ModelAdmin):
    list_display = (
        "__str__",
        "created",
    )
