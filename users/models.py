from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Definition User Model (extend AbstractUser)"""

    address = models.CharField(max_length=50)
    about_me = models.TextField(default="")
    avatar = models.ImageField(upload_to="avatars", blank=True)
    id_checked = models.BooleanField(default=False)
    birthday = models.DateField(null=True)

    def buyer_average(self):
        seller_reviews = self.seller.all()
        if len(seller_reviews) == 0:
            return 0
        else:
            total = 0
            for review in seller_reviews:
                total += review.rating_average()
            return round(total / len(seller_reviews), 2)

    buyer_average.short_description = "AVG"
