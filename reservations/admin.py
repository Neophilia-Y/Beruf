from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class AdminReservation(admin.ModelAdmin):

    list_display = ("product", "status", "appointment", "left_days")
