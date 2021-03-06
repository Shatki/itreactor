# Generated by Django 3.1.3 on 2020-12-06 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201203_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name='имя')),
            ],
            options={
                'verbose_name': 'ключевое слово',
                'verbose_name_plural': 'ключевые слова',
                'db_table': 'tips',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='tips',
            field=models.ManyToManyField(null=True, to='blog.Tips', verbose_name='ключевые слова'),
        ),
    ]
