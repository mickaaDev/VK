from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from languages.fields import LanguageField
from django.db.models.signals import post_save, pre_save


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

    def get_absolute_url(self):
        return reverse("core:core-detail", kwargs={"pk":self.pk})

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
        verbose_name="Пользователь",
    )

    bday = models.DateField(
        null=True,
        auto_now=False,
        auto_now_add=False,
    )
    
    description = models.TextField(
        null=True,blank=True,
        verbose_name="О себе"
    )

    photo = models.ImageField(
        null=True, 
        default="default-profile.jpg",
        upload_to="static/images",
        verbose_name="Фото профиля"
    )
    city = models.CharField(
        max_length=255,
        null=True, blank=True,
        verbose_name="Город"
    )
    
    CATEGORY_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('None', 'None')
    )

    gender = models.CharField(
        max_length=200, null=True, 
        choices=CATEGORY_CHOICES,
        verbose_name="Пол"
    )

    institution = models.CharField(
        max_length=255, 
        null=True, blank=True,
        verbose_name="Учреждение"

    )

    CATEGORY_RELATIONSHIP = (
        ('None selected', 'None selected'),
        ('Unmarried', 'Unmarried'),
        ('In a relationship', 'In a relationship'),
        ('Engaged', 'Engaged'),
        ('Married', 'Married'),
        ('In a civil union', 'In a civil union'),
        ('In love', 'In love'),
        ('Its complicated', 'Its complicated '),
        ('Actively searching', 'Actively searching'),
    )

    relationship = models.CharField(
        max_length=200, null=True, 
        choices=CATEGORY_RELATIONSHIP,
        verbose_name="Отношения"
    )

    language = LanguageField(
        max_length=255, null=True,blank=True, 
        verbose_name="Язык"
    )
    

    CATEGORY_FAMILY = (
        ('Grandparents', 'Grandparents'),
        ('Parents', 'Parents'),
        ('Siblings', 'Siblings'),
        ('Children', 'Children'),
        ('Grandchildren', 'Grandchildren'),
    )

    families = models.CharField(
        max_length=255, null=True,
        choices=CATEGORY_FAMILY,
        verbose_name="Семья"
    )

def create_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
        print('Profile created!')

post_save.connect(create_profile,sender=User)


