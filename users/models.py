# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.core.mail import EmailMessage
from itreactor.validators import e_mail
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from itreactor.settings import PROFILE_PHOTOS_DIR, PROFILE_PHOTO_DEFAULT_NAME
# from web.models import MailSet


# Класс менеджера должен переопределить методы create_user() и create_superuser().
class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Создает и сохраняет пользователя с введенным им email и паролем.
        """
        if not email:
            raise ValueError(u'e-mail должен быть указан')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


# Create your models here.
class User(AbstractUser):
    class Meta:
        verbose_name = u'пользователь'
        verbose_name_plural = u'пользователи'
        db_table = u'users'

    # Авторизация будет происходить по E-mail
    email = models.EmailField(verbose_name=u'электронная почта', unique=True, max_length=255)
    # Имя - не является обязательным
    first_name = models.CharField(verbose_name=u'имя пользователя', max_length=40, blank=True, null=True)
    # Фамилия - также не обязательна
    last_name = models.CharField(verbose_name=u'фамилия пользователя', max_length=40, blank=True, null=True)

    photo = models.ImageField(upload_to=PROFILE_PHOTOS_DIR, verbose_name=u'фото', blank=True, null=True,
                              default=PROFILE_PHOTO_DEFAULT_NAME)
    # Атрибут суперпользователя
    is_admin = models.BooleanField(default=False, null=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(verbose_name=u'дата создания', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name=u'последнее обновление', auto_now=True)

    objects = UserManager()
    username = None

    # логинимся
    USERNAME_FIELD = 'email'
    # обязательное поле
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return u'%s' % self.email

    def __str__(self):
        return u'%s' % self.email

    def get_photo(self):
        return self.photo

    def get_full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def send_email(self, name=u'Anonymus', from_email=None, subject=u'None', message=u'None', **kwargs):
        """
        Отправляет электронное письмо этому пользователю.
        """
        # Настраиваем шлюз
        email_subject = u'Пользователь %s<%s> оставил сообщение на сате на тему: %s' % (name, from_email, subject)
        html = u'<p><h3>%s</h3></p>' % message
        email = EmailMessage(email_subject, html, from_email, [self.email], **kwargs)
        email.content_subtype = "html"  # Main content is now text/html
        email.send()
        return

    def has_perm(self, perm, obj=None):
        return True


class Feedback(models.Model):
    class Meta:
        verbose_name = u"сообщение с формы обратной связи"
        verbose_name_plural = u'сообщения с формы обратной связи'
        db_table = u'feedback'

    name = models.CharField(verbose_name=u'имя', max_length=100)
    email = models.CharField(verbose_name=u'email', max_length=50)
    subject = models.CharField(verbose_name=u'тема сообщения', max_length=100)
    message = models.CharField(verbose_name=u'текст сообщения', max_length=400)
    date = models.DateTimeField(verbose_name=u'время отправки', auto_now_add=True)

    def __str__(self):
        return u"Автор:%s, тема сообщения:%s" % (self.name, self.subject)

    def __unicode__(self):
        return u'%s' % self.name
