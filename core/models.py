from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from allauth.account.signals import user_logged_in

User = get_user_model()


def user_logged_in_reciever(request, user, **kwargs):
    print(user)

user_logged_in.connect(user_logged_in_reciever, sender=User)



class BaseModel(models.Model):
    name = models.CharField(
        max_length=255,
        null=True,
        verbose_name="имя"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )

    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата изменения"
    )

    deleted = models.BooleanField(
        default=False,
        verbose_name="Удалено"
    )

    def __str__(self):
        if self.name:
            return self.name
        return f"Обьект{self.pk}"

    class Meta:
        abstract = True


class Profile(BaseModel):
    user = models.OneToOneField(
        to=User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="profile",
        verbose_name="Пользователь"
    )

    bday = models.DateField(
        null=True,
        auto_now=False,
        auto_now_add=False,
    )

    subscription = models.ManyToManyField(
        to=User,
        blank=True, 
        related_name="subscriber",
        verbose_name="Подписка"
    )

    description = models.TextField(
        null=True,blank=True,
        verbose_name="О себе"
    )

    photo = models.ImageField(
        null=True, blank=True,
        default="media/default-profile.jpg",
        upload_to="profile",
        verbose_name="Фото профиля"
    )
    city = models.CharField(
        max_length=255,
        null=True, blank=True,
        verbose_name="Город"
    )
    
    CATEGORY_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'None')
    )

    gender = models.CharField(max_length=200, null=True, choices=CATEGORY_CHOICES)

    institution = models.CharField(
        max_length=255, 
        null=True, blank=True,
        verbose_name="institution"
    )
    


    



