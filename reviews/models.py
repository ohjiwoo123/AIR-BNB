from django.db import models
from core import models as core_models

# Create your models here.


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        # 지린다.... 포린키의 위엄 , 세개의 레이어에 접근하고, relationship의 힘이다.
        # return self.room.host.email
        return f"{self.review} - {self.room}"

    def rating_average(self):
        avg = (
            self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)
