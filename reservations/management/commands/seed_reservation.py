from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from products import models as product_models
from reservations import models as reservation_models
import random


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many lists do you want to create"
        )

    def handle(self, *args, **option):
        users = User.objects.all()
        products = product_models.Product.objects.all()
        number = option.get("number")
        seeder = Seed.seeder()

        seeder.add_entity(
            reservation_models.Reservation,
            number,
            {
                "buyer": lambda x: random.choice(users),
                "product": lambda x: random.choice(products),
                "appointment": lambda x: datetime.now()
                + timedelta(days=random.randint(3, 25)),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} reservations created"))
