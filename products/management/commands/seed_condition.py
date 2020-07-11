from django.core.management.base import BaseCommand
from products.models import Condition


class Command(BaseCommand):
    conditions = ["send box", "visit", "cash", "online banking", "etc.."]
    current_list = [obj.name for obj in Condition.objects.all()]

    def handle(self, *args, **option):

        for c in self.conditions:
            if c not in self.current_list:
                Condition.objects.create(name=c)

        self.stdout.write(self.style.SUCCESS("Condition list created"))
