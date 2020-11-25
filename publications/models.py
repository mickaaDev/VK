from django.db import models
from django.contrib.auth.models import User
from core.models import *

class Publication(models.Model):
    publisher = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="publication",
        verbose_name="владелец"
    )
    description = models.TextField(
        null=True,blank=True,
        verbose_name="Описание"
    )
    image = models.ImageField(
        null=True,blank=True,
        upload_to="publications",
        verbose_name="Фото"
    )
    views = models.IntegerField(
        default=0
    )
    avialable = models.BooleanField(
        default=True,
        verbose_name="Есть в наличии"
    )
    likes = models.ManyToManyField(
        to=User,
        related_name="like",
        verbose_name="понравилось"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления",
    )




    