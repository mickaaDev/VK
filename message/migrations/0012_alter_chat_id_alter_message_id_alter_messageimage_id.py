# Generated by Django 4.0 on 2022-01-22 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0011_auto_20201117_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='messageimage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]