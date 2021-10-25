from django.contrib import admin
from . import models

# RoomType 옆에 + 버튼 생김
@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass


# Register your models here.
# Host 옆에 + 버튼 생김
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Spaces",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        (
            "Last Details",
            # host 옆에 ,를 붙여줘야 List로 인식한다.(단일 인자인 경우)
            {"fields": ("host",)},
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    # https://docs.djangoproject.com/en/3.2/ref/contrib/admin/
    # search_fields 참고 , 인자의 default = icontains 이다. (icontains 는 insensitive를
    # 포함한다, 대소문자 구분을 안함, SEO만 입력해도 seoul을 반환함)
    search_fields = ("=city", "^host__username")

    filter_horizontal = ("amenities", "facilities", "house_rules")

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    # count_amenities.short_description = "hello sexy!"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""

    pass
