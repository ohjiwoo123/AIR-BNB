from django.core.management.base import BaseCommand
from rooms.models import Facility

# from rooms import models as room_models 도 가능, 위에 as는 임의의 이름을 붙이는 것


class Command(BaseCommand):
    help = "This Command creates facilities"

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created!"))
