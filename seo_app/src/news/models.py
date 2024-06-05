import os
import uuid
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

from ..core.models import AnonymousUser
from ..users.models import Person

class PublishedManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('article/', filename)


class Article(models.Model):

    title = models.CharField(max_length=255, unique=True, verbose_name="Заголовок")
    article = RichTextUploadingField(verbose_name="Содержание")
    views = models.BigIntegerField(verbose_name='Просмотров')
    likes = models.BigIntegerField(verbose_name='Понравилось')
    dis_likes = models.BigIntegerField(verbose_name='Не понравилось')
    image = models.ImageField(upload_to=get_file_path, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return f"{str(self.pk)}: {self.title}"

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]

    def get_absolute_url(self):
        return reverse('article', kwargs={'slug': self.slug})


class DataArticle(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    user_anonim = models.ForeignKey(AnonymousUser, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ViewArticle(DataArticle):
    ...


class LikeArticle(DataArticle):
    ...


class DisLikeArticle(DataArticle):
    ...

