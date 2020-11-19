from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="feedback",
        verbose_name="от кого"
    )
    text = models.TextField()
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления",
    )



