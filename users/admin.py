#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm
from .models import User, Feedback


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        'email',
        'first_name',
        'last_name',
        'last_login')

    list_filter = (
        'date_joined',
        'last_login',
    )
    readonly_fields = (
        'date_joined',
        'date_updated',
        'last_login',
    )

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            )
        }),

        (u'Персональная информация', {
            'fields': (
                'first_name',
                'last_name',
                'photo',
            )
        }),

        (u'Права доступа', {
            'fields': (
                'groups',
                'user_permissions',
                'is_superuser',
                'is_staff',
                'is_active',
            )
        }),

        (u'Важные даты', {
            'fields': (
                'last_login',
                'date_joined',
                'date_updated',
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes':
                ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'is_superuser',
            )
        }),
    )

    search_fields = (
        'email',)

    ordering = (
        'date_joined',)

    filter_horizontal = (
        'groups',
        'user_permissions',
    )


# Register your models here.
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'date',
                    'email',
                    'subject',
                    'message',
                    )

    search_fields = ('name',)
    ordering = ('date',)
