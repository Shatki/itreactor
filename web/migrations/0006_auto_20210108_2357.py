# Generated by Django 3.1.3 on 2021-01-08 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20210108_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='hero_label',
            field=models.CharField(default='Разработка IT проектов', max_length=100, verbose_name='hero: деятельность'),
        ),
        migrations.AlterField(
            model_name='website',
            name='hero_text',
            field=models.CharField(default='Наша IT мастерская предлагает свои услуги по созданию сайтов, интернет проектов и сервисов, SEO оптимизации в сети Интернет. Используем только самые передовые технологии разработки, и гарантируем превосходные результат по адекватным ценам.', max_length=200, verbose_name='hero: описание деятельности'),
        ),
    ]