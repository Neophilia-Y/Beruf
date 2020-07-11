from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
from users.models import User
from lists import models as list_models
from products import models as product_models
import random


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many lists do you want to create"
        )

    def handle(self, *args, **option):
        users = User.objects.all()
        product_count = product_models.Product.objects.count()
        number = option.get("number")
        seeder = Seed.seeder()

        seeder.add_entity(
            list_models.List, number, {"user": lambda x: random.choice(users),},
        )
        list_pk = seeder.execute()
        clear_list_pk = flatten(list(list_pk.values()))

        for pk in clear_list_pk:
            current_list = list_models.List.objects.get(pk=pk)
            random_num_list = []
            for _ in range(1, 5):
                random_number = random.randint(0, product_count - 1)
                if random_number not in random_num_list:
                    random_num_list.append(random_number)
                    current_list.product.add(
                        product_models.Product.objects.all()[random_number]
                    )
        self.stdout.write(self.style.SUCCESS(f"{number} lists created"))
