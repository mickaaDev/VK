from django.db.models.signals import post_save, pre_save, post_delete
from django.contrib.auth.models import User
from .models import Profile


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            name=instance.username,
            username=instance.username
        )
        print('Profile created')


def update_profile(sender, instance, created, **kwargs):
    user_profile, _ = Profile.objects.get_or_create(user=instance)
    if not created:

        user_profile.username = instance.username

        user_profile.save()
        print('Profile updated!')


post_save.connect(create_profile, sender=User)
post_save.connect(update_profile, sender=User)
