# Generated by Django 3.1.3 on 2021-01-08 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20210108_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='contact_text',
            field=models.TextField(default='', max_length=500, verbose_name='contact: текст'),
        ),
        migrations.AlterField(
            model_name='website',
            name='hero_text',
            field=models.TextField(default='Наша IT мастерская предлагает свои услуги по созданию сайтов, интернет проектов и сервисов, SEO оптимизации в сети Интернет. Используем только самые передовые технологии разработки, и гарантируем превосходные результат по адекватным ценам.', max_length=400, verbose_name='hero: описание деятельности'),
        ),
    ]
