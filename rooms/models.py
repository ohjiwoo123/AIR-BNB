from django.db import models
from django_countries.fields import CountryField
from django.urls import reverse
from core import models as core_models
from users import models as user_models

# 처음은 파이썬 관련, 다음은 장고, 외부패키지, 내가 만든 패키지
# Create your models here.


class AbstractItem(core_models.TimeStampedModel):
    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """RoomType Model Definition"""

    class Meta:
        # verbose_name = 무엇...?
        verbose_name = "Room Type"
        # ordering = 정렬하는 데 created, name 등등의 조건으로 가능
        # ordering = ["created"]


class Amenity(AbstractItem):
    """Amenity Model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """HouseRule Model Definition"""

    class Meta:
        verbose_name = "House Rule"


class Room(core_models.TimeStampedModel):
    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField(help_text="How many people will be staying?")
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # ForeingKey는 한 모델을 다른 모델과 연결시켜주는 역할을 한다. (일 대 다)
    # on_delete은 User가 삭제 될 경우 어떤 조치를 취할 것인가 이다. CASCADE = 폭포수라는 의미, 폭포수 처럼 모두 삭제된다는 뜻
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    # 모델을 여러개 선택이가능하다. ex) 쉐어룸 호텔룸 등등 다양한 룸 형식을 한 번에 적용 가능
    room_type = models.ForeignKey(
        "RoomType", related_name="room_type", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0


# 파이썬은 파일을 상하 수직방향으로 읽기 때문에 포토 클래스가 룸 클래스 밑에 있어야 한다.(아래에 room = models.ForeignKey(Room)인자를 사용하기 위해서)
class Photo(core_models.TimeStampedModel):
    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    # 내가 room을 지우면 사진도 연결되어있기 때문에 함께 지워져야 한다.
    # "Room" string으로 사용할 수도 있다.
    # room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
