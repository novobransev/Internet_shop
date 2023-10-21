from django.contrib import admin
from django.utils.html import format_html

from .models import Product, Category, Country, Ip

admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Ip)


@admin.register(Product)
class ProfileAdmin(admin.ModelAdmin):

    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:60px; max-height:50px"/>'.format(obj.image.url))
        else:
            return None

    list_display = ('name', 'price', 'quantity', 'rating_products', 'get_image')
    readonly_fields = ['get_image']

    get_image.short_description = 'Изображение'
