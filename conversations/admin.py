from django.contrib import admin
from . import models


@admin.register(models.Conversation)
class AdminConversation(admin.ModelAdmin):
    pass


@admin.register(models.Message)
class AdminMessage(admin.ModelAdmin):
    pass
