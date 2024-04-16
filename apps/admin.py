from django.contrib.admin import StackedInline, ModelAdmin
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.safestring import mark_safe

from apps.forms import ProductModelForm
from apps.models import Category, Product, ProductImages


# Register your models here.
@admin.register(Category)
class CategoryUserAdmin(admin.ModelAdmin):
    search_fields = ['name']


class ProductImagesStackedInline(StackedInline):
    model = ProductImages
    min_num = 1
    extra = 0
    fields = ['image', ]


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = (ProductImagesStackedInline,)
    form = ProductModelForm
    list_display = ['name', 'category', 'sell_price', 'image_show']
    list_per_page = 10
    list_max_show_all = 20

    def image_show(self, obj: Product):
        if obj.images.first():
            return mark_safe(
                "<img src='{}' width='100' height='100' />".format(obj.images.first().image.url))

        return ''

    image_show.description = 'images'
