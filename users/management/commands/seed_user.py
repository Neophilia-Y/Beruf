from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many users do you want to create"
        )

    def handle(self, *args, **option):
        number = option.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(
            User,
            number,
            {
                "address": lambda x: seeder.faker.city(),
                "is_staff": False,
                "is_superuser": False,
                "avatar": None,
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} created"))
