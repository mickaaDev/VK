from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Gallery_item(models.Model):
    publisher = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="gallery_item",
        verbose_name="владелец"
    )
    description = models.TextField(
        null=True,blank=True,
        verbose_name="Описание"
    )
    image = models.ImageField(
        blank=False,
        upload_to="gallery",
        verbose_name="Фото"
    )
    avialable = models.BooleanField(
        default=True,
        verbose_name="виден всем"
    )
    likes = models.ManyToManyField(
        to=User,
        related_name="gallery_like",
        verbose_name="Понравилось"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления",
    )


