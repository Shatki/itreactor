# Generated by Django 3.1.3 on 2021-01-01 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='наименование настроек')),
                ('slogan', models.CharField(max_length=100, verbose_name='слоган')),
            ],
            options={
                'verbose_name': 'настройка сайта',
                'verbose_name_plural': 'настройки сайта',
            },
        ),
    ]