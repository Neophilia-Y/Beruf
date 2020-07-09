from django.db import models
from users import models as user_models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):
    """Working Condition class"""

    name = models.CharField(max_length=40)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(AbstractItem):
    """Task Type Model"""

    pass

    class Meta:
        verbose_name_plural = "Category"
        ordering = ["name"]


class Condition(AbstractItem):
    """Condtion cash, visit, parcel, onlineBanking ..what else"""

    pass


class Photo(core_models.TimeStampedModel):
    """Product Photo Model"""

    caption = models.CharField(max_length=50)
    files = models.ImageField(upload_to="product_photos")
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Product(core_models.TimeStampedModel):
    """Model Product"""

    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=1000)  # Use MinValueValidator
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    condition = models.ManyToManyField(Condition)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.host}'s product"

    def save(self, *args, **kwargs):
        self.title = str.capitalize(self.title)
        super().save(*args, **kwargs)  # Call the real save() method

