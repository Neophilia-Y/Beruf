from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):
    """List Model Definition"""

    name = models.CharField(max_length=30)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    product = models.ManyToManyField("products.Product", blank=True)

    def __str__(self):
        return self.name

    def product_count(self):
        return self.product.count()

    product_count.short_description = "Number of product"
