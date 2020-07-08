from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Definition User Model (extend AbstractUser)"""

    address = models.CharField(max_length=50)
    about_me = models.TextField(default="")
    avatar = models.ImageField(blank=True)
    id_checked = models.BooleanField(default=False)
    birthday = models.DateField(null=True)
