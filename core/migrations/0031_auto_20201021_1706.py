# Generated by Django 3.1.2 on 2020-10-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20201021_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='families',
            field=models.CharField(choices=[('Grandparents', 'Grandparents'), ('Parents', 'Parents'), ('Siblings', 'Siblings'), ('Children', 'Children'), ('Grandchildren', 'Grandchildren')], max_length=255, null=True, verbose_name='Семья'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('None', 'None')], max_length=200, null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='relationship',
            field=models.CharField(choices=[('None selected', 'None selected'), ('Unmarried', 'Unmarried'), ('In a relationship', 'In a relationship'), ('Engaged', 'Engaged'), ('Married', 'Married'), ('In a civil union', 'In a civil union'), ('In love', 'In love'), ('Its complicated', 'Its complicated '), ('Actively searching', 'Actively searching')], max_length=200, null=True, verbose_name='Отношения'),
        ),
    ]