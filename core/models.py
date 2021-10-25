from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    """Time Stamped Model"""

    # auto_now_add : 생성시 자동으로 시간을 입력해줌
    # auto_now : 수정(저장)시 자동으로 시간을 입력해줌
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
