import uuid

from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):

    """Class which specifies superuser"""

    def create_user(self, username, password, **kwargs):
        user = self.model(username=username, **kwargs)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.set_password(kwargs['password'])
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        default=''
    )
    name = models.CharField(
        max_length=255,
        null=True,
    )
    email = models.EmailField(
        verbose_name='Email',
        unique=True
    )
    username = models.CharField(
        max_length=255,
        null=True
    )
    image = models.ImageField(
        blank=True,
        null=True,
        default='123.jpg'
    )
    bio = models.TextField(
        null=True
    )
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
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
        verbose_name="Relationship"
    )
    CATEGORY_FAMILY = (
        ('Grandparents', 'Grandparents'),
        ('Parents', 'Parents'),
        ('Siblings', 'Siblings'),
        ('Children', 'Children'),
        ('Grandchildren', 'Grandchildren'),
    )

    families = models.CharField(
        max_length=255, null=True, blank=True,
        choices=CATEGORY_FAMILY,
        verbose_name="Family"
    )
    city = models.CharField(
        max_length=255,
        null=True, blank=True,
        verbose_name="City"
    )

    CATEGORY_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('None', 'None')
    )

    gender = models.CharField(
        max_length=200, null=True,
        choices=CATEGORY_CHOICES,
        verbose_name="Gender"
    )
    slug = models.SlugField(default='')

    bday = models.DateField(
        null=True,
    )

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return str(self.user.username)


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('Profile created!')


post_save.connect(create_profile, sender=User)
