from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
from products import models as product_models
from users.models import User
import random


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many products do you want to create",
        )

    def handle(self, *args, **option):
        number = option.get("number")
        seeder = Seed.seeder()
        all_users = User.objects.all()
        categories = product_models.Category.objects.all()
        conditions = product_models.Condition.objects.all()
        seeder.add_entity(
            product_models.Product,
            number,
            {
                "host": lambda x: random.choice(all_users),
                "title": lambda x: seeder.faker.company(),
                "price": lambda x: 1000 * random.randint(1, 20),
                "category": lambda x: random.choice(categories),
            },
        )
        product_pk = seeder.execute()
        clear_pk = flatten(list(product_pk.values()))
        for pk in clear_pk:
            product = product_models.Product.objects.get(pk=pk)
            for _ in range(random.randint(4, 8)):
                product_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    product=product,
                    files=f"/product_photos/{random.randint(1,32)}.webp",
                )

            for condition in conditions:
                random_number = random.randint(0, 10)
                if random_number % 2 == 0:
                    product.condition.add(condition)
        self.stdout.write(self.style.SUCCESS(f"{number} created"))
