from django.db import models
from core import models as core_models
from django.utils import timezone


class Reservation(core_models.TimeStampedModel):
    """Reservation Model Definition"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Comfirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    buyer = models.ForeignKey("users.User", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    appointment = models.DateField()

    def __str__(self):
        return f"{self.product} - {self.appointment}"

    def left_days(self):
        now = timezone.now().date()
        return str(self.appointment - now).split()[0]
