# Generated by Django 3.1.2 on 2020-10-14 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20201014_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='media/default-profile.jpg', null=True, upload_to='profile', verbose_name='Фото профиля'),
        ),
    ]