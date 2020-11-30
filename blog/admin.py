#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Article, Comment


# Register your models here.
@admin.register(Article)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'added',
                    'fix',
                    )

    search_fields = ('title',)
    ordering = ('added',
                'title'
                )


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author',
                    'allowed',
                    'added',
                    'article',
                    'reply'
                    )

    search_fields = ('article', 'added')
    ordering = ('article', 'added')
    list_filter = ('article', 'added')
