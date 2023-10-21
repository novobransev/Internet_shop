from django.contrib import admin
from django.utils.html import format_html

from .models import City, Profile


admin.site.register(City)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    def get_image(self, obj):
        if obj.profile_pic:
            return format_html('<img src="{}" style="max-width:60px; max-height:50px"/>'.format(obj.profile_pic.url))
        else:
            return None

    list_display = ('user', 'city', 'get_image')
    readonly_fields = ['get_image']

    get_image.short_description = 'Изображение'



