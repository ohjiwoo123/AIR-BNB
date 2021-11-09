from django.core.management.base import BaseCommand
from rooms.models import Amenity

# from rooms import models as room_models 도 가능, 위에 as는 임의의 이름을 붙이는 것


class Command(BaseCommand):
    help = "This Command creates amenities"

    def handle(self, *args, **options):
        amenities = [
            "Air conditioning",
            "Alarm Clock",
            "Balcony",
            "Bathroom",
            "Bathtub",
            "Bed Linen",
            "Boating",
            "Cable TV",
            "Carbon monoxide detectors",
            "Chairs",
            "Children Area",
            "Coffe Maker in Room",
            "Cooking Hub",
            "Dish Washer",
            "Double bed",
            "En suite bethroom",
            "Free Parking",
            "Free Wireless Internet",
            "Freezer",
            "Fridge / Freezer",
            "Golf",
            "Hair Dryer",
            "Heating",
            "Hot tub" "Hot tub" "Indoor Pool",
            "Microwave",
            "Outdoor Pool",
            "Outdoor Tennis",
            "Oven",
            "Queen size bed",
            "Restaurant",
            "Shoping Mall",
            "Shower",
            "Smoke Detector",
            "Sofa",
            "Streo",
            "Swimming Pool",
            "Toilet",
            "Towels",
            "TV",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created"))
