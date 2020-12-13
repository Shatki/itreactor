#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from django.db import models
from PIL import Image
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from itreactor.settings import ARTICLE_PHOTOS_DIR, PROFILE_PHOTOS_DIR, ARTICLE, NO_PHOTO, MEDIA_ROOT, MEDIA_URL
from users.models import User
from ckeditor.fields import RichTextField
from django.db.models.signals import m2m_changed


class Tips(models.Model):
    class Meta:
        verbose_name = u'ключевое слово'
        verbose_name_plural = u'ключевые слова'
        db_table = u'tips'

    name = models.CharField(max_length=60, verbose_name=u'имя', unique=True, blank=False, null=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name


# Create your models here.
class Article(models.Model):
    class Meta:
        verbose_name = u'статья'
        verbose_name_plural = u'статьи'
        db_table = u'article'

    title = models.CharField(max_length=200, verbose_name=u'заголовок')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    added = models.DateTimeField(verbose_name=u'время добавления', auto_now_add=True)
    updated = models.DateTimeField(verbose_name=u'последнее обновление', auto_now=True)
    photo = models.ImageField(upload_to=ARTICLE_PHOTOS_DIR, verbose_name=u'фотография', name='photo', blank=False)
    tips = models.ManyToManyField(Tips, verbose_name=u'ключевые слова')

    fix = models.BooleanField(u'закрепить статью как основную', default=False, blank=True)
    text = RichTextField(verbose_name=u'текст статьи')

    def save(self, *args, **kwargs):
        Article.objects.all().update(fix=False)
        super(Article, self).save(*args, **kwargs)
        # Create a thumb
        im = Image.open(self.photo)
        im.thumbnail((200, 200))
        im.save("%s/%s%s" % (MEDIA_ROOT, ARTICLE_PHOTOS_DIR, self.thumb_name()))

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.title

    def url(self):
        return u'%s/%s/' % (ARTICLE, self.id)

    def absolute_url(self):
        return u'/%s/%s/' % (ARTICLE, self.id)

    def photo_name(self):
        return os.path.basename(self.photo.name)

    def thumb_name(self):
        return "thumbnail_%s" % self.photo_name()

    def thumb_url(self):
        return "%s%sthumbnail_%s" % (MEDIA_URL, ARTICLE_PHOTOS_DIR, self.photo_name())

    def date(self):
        return u'{:0>2}/{:0>2}/{:0>2}'.format(str(self.added.day), str(self.added.month), str(self.added.year))

    def view_tips(self):
        return ', '.join([str(i) for i in self.tips.all()])

    def count_comments(self):
        return Comment.objects.filter(article=self).count()

    def clean_fields(self, exclude=None):
        # todo: Нужно доработать
        super().clean_fields(exclude=exclude)
        if self.tips.count() > 4:
            raise ValidationError({'tips': _("You can't assign more than 4 tips")})


class Comment(models.Model):
    class Meta:
        verbose_name = u'комментарий'
        verbose_name_plural = u'комментарии'
        db_table = u'comments'

    # комментатор
    author = models.CharField(max_length=50, verbose_name=u'имя комментатора')
    email = models.EmailField(verbose_name=u'электронная почта')
    added = models.DateTimeField(verbose_name=u'время добавления', auto_now_add=True)
    allowed = models.BooleanField(verbose_name=u'разрешение на публикацию', default=False)
    article = models.ForeignKey(Article, verbose_name=u'комментируемая новость', on_delete=models.CASCADE,
                             blank=False, null=False)
    reply = models.ForeignKey('self', verbose_name=u'ответ на комментарий', on_delete=models.CASCADE,
                              blank=True, null=True)
    message = RichTextField(verbose_name=u'текст комментария', blank=False, null=False)
    photo = models.ImageField(upload_to=PROFILE_PHOTOS_DIR, verbose_name=u'фотография профиля', blank=True)

    def __str__(self):
        return u'%s %s' % (self.added, self.author)

    def __unicode__(self):
        return u'%s %s' % (self.added, self.author)

    def save(self, *args, **kwargs):
        try:
            self.photo = User.objects.get(email=self.email).photo
        except User.DoesNotExist:
            self.photo = None
        super(Comment, self).save(*args, **kwargs)


def get_article(tag=None):
    # Включая сортировку по тегу
    if not tag:
        articles = Article.objects.all().order_by('added')
    else:
        articles = Article.objects.filter(tips__id=tag).order_by('added')

    # Сортировка новостей
    articles_sort = []
    fix = None
    for article in articles:
        if article.fix:
            fix = article
        else:
            articles_sort.append(article)

    if fix is not None:
        articles_sort.append(fix)

    articles_sort.reverse()
    return articles_sort


def regions_changed(sender, **kwargs):
    if kwargs['instance'].tips.count() > 4:
        raise ValidationError({'tips': _("You can't assign more than 4 tips")})


m2m_changed.connect(regions_changed, sender=Article.tips.through)

