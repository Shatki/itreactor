from django.contrib import admin
from .models import Website


# Register your models here.
@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'slogan',
                    'hero_label',
                    'hero_text',

                    'contact_text',
                    'contact_name',
                    'contact_address',
                    'contact_phone',
                    'contact_email',
                    'contact_vk',
                    'contact_youtube',
                    'contact_telegram',
                    'contact_twitter',

                    )

    search_fields = ('name',)
    ordering = ('name',)


