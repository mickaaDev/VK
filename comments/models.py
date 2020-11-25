from django.db import models
from django.contrib.auth.models import User
from publications.models import *
from core.models import BaseModel 

# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    publication_com = models.ForeignKey(
        to=Publication,
        on_delete=models.CASCADE,
        related_name="comment",
        verbose_name="Публикация"
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="comment",
        verbose_name="от кого"
    )
    likes = models.ManyToManyField(
        to=User,
        related_name="comment_like",
        verbose_name="Понравился этот коментарий"
    )

    @property 
    def number_of_likes(self):
        return self.likes.count()


    