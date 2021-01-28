from django.db import models

# Create your models here.


class Website(models.Model):
    class Meta:
        verbose_name = 'настройка сайта'
        verbose_name_plural = 'настройки сайта'

    # Название настроек сайта
    name = models.CharField(verbose_name='наименование настроек', max_length=50)
    hero_label = models.CharField(verbose_name='hero: деятельность', max_length=100, default='Разработка IT проектов')
    # Наша IT мастерская предлагает услуги по созданию сайтов, интернет проектов и сервисов, SEO оптимизации в сети
    # Интернет. Используем только самые передовые технологии разработки и гарантируем
    # превосходный результат по адекватным ценам.
    hero_text = models.TextField(verbose_name='hero: описание деятельности', max_length=400, default='')

    slogan = models.CharField(verbose_name='слоган', max_length=100)
    # Контактная информация
    contact_text = models.TextField(verbose_name='contact: текст', max_length=500, default='')
    contact_name = models.CharField(verbose_name='contact: имя', max_length=150, default='')
    contact_address = models.CharField(verbose_name='contact: адрес', max_length=150, default='')
    contact_phone = models.CharField(verbose_name='contact: телефон', max_length=20, default='')
    contact_email = models.CharField(verbose_name='contact: email', max_length=100, default='')

    # Соцсети
    contact_youtube = models.CharField(verbose_name='info: ютуб', max_length=100, default='')
    contact_vk = models.CharField(verbose_name='info: вконтакте', max_length=100, default='')
    contact_telegram = models.CharField(verbose_name='info: телеграмм', max_length=100, default='')
    contact_twitter = models.CharField(verbose_name='info: твиттер', max_length=100, default='')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name
