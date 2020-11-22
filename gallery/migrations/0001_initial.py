# Generated by Django 3.1.3 on 2020-11-19 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='gallery', verbose_name='Фото')),
                ('avialable', models.BooleanField(default=True, verbose_name='виден всем')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('likes', models.ManyToManyField(related_name='gallery_like', to=settings.AUTH_USER_MODEL, verbose_name='Понравилось')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_item', to=settings.AUTH_USER_MODEL, verbose_name='владелец')),
            ],
        ),
    ]
