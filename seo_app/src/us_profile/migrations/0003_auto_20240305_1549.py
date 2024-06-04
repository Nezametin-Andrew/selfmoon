# Generated by Django 3.2 on 2024-03-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('us_profile', '0002_auto_20240305_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=255, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='media/users/avatars/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=255, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=255, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gmail',
            field=models.EmailField(blank=True, max_length=254, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='job',
            field=models.CharField(blank=True, max_length=255, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=255, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tg',
            field=models.CharField(blank=True, max_length=255, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='vk',
            field=models.CharField(blank=True, max_length=255, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='yandex',
            field=models.EmailField(blank=True, max_length=254, verbose_name=''),
        ),
    ]
