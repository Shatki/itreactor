# Generated by Django 3.1.3 on 2020-11-14 21:58

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='заголовок')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='время добавления')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='последнее обновление')),
                ('photo', models.ImageField(upload_to='news/', verbose_name='фотография')),
                ('fix', models.BooleanField(blank=True, default=False, verbose_name='закрепить статью как основную')),
                ('text', ckeditor.fields.RichTextField(verbose_name='текст статьи')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, verbose_name='имя комментатора')),
                ('email', models.EmailField(max_length=254, verbose_name='электронная почта')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='время добавления')),
                ('allowed', models.BooleanField(default=False, verbose_name='разрешение на публикацию')),
                ('message', ckeditor.fields.RichTextField(verbose_name='текст комментария')),
                ('photo', models.ImageField(blank=True, upload_to='photos/', verbose_name='фотография профиля')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article',
                                              verbose_name='комментируемая новость')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                            to='blog.comment', verbose_name='ответ на комментарий')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
                'db_table': 'comments',
            },
        ),
    ]
