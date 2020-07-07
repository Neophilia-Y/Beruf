from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Definition User Model (extend AbstractUser)"""

    EXP_NEW = "new"
    EXP_THREE_MONTH = "3 months"
    EXP_SIX_MONTH = "1-6 months"
    EXP_ONE_YEAR = "6-12 years"
    EXP_FIVE_YEAR = "5 years"
    EXP_TEN_YEAR = "10 years"

    EXP_CHOICES = (
        (EXP_NEW, "New"),
        (EXP_THREE_MONTH, "Under 3 months"),
        (EXP_SIX_MONTH, "1-6 months"),
        (EXP_ONE_YEAR, "6-12 years"),
        (EXP_FIVE_YEAR, "Under 5 year"),
        (EXP_TEN_YEAR, "Over 10 year"),
    )

    ENGINEER = "engineer"
    DESIGNER = "designer"
    PROFESSOR = "professor"

    EXPERTISE = (
        (ENGINEER, "Engineer"),
        (DESIGNER, "Designer"),
        (PROFESSOR, "Professor"),
    )

    experience = models.CharField(blank=True, choices=EXP_CHOICES, max_length=20)
    expertise = models.CharField(blank=True, max_length=10, choices=EXPERTISE,)
    about_me = models.TextField(default="")
    avatar = models.ImageField(blank=True)
    id_checked = models.BooleanField(default=False)
    birthday = models.DateField(null=True)
