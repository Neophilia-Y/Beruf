from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from reviews import models as review_models
import random


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many users do you want to create"
        )

    def handle(self, *args, **option):
        number = option.get("number")
        seeder = Seed.seeder()
        buyers = User.objects.all()
        sellers = User.objects.exclude(product__isnull=True)  # 상품을 판 사용자만 정의

        seeder.add_entity(
            review_models.Review,
            number,
            {
                "buyer": lambda x: random.choice(buyers),
                "seller": lambda x: random.choice(sellers),
                "accuracy": lambda x: random.randint(1, 5),
                "communication": lambda x: random.randint(1, 5),
                "manner": lambda x: random.randint(1, 5),
                "quality": lambda x: random.randint(1, 5),
                "appointment": lambda x: random.randint(1, 5),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created"))
