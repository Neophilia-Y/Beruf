from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):
    """Review Model Definition"""

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    manner = models.IntegerField()
    quality = models.IntegerField()
    appointment = models.IntegerField()
    buyer = models.ForeignKey(
        "users.User", related_name="buyer", on_delete=models.CASCADE
    )
    seller = models.ForeignKey(
        "users.User", related_name="seller", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"buyer:{self.buyer} seller:{self.seller}"

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.manner
            + self.quality
            + self.appointment
        ) / 5
        return round(avg, 2)


class Comment(core_models.TimeStampedModel):
    """Comment Model Definition"""

    comment = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
