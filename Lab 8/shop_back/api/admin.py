from django.contrib import admin

from api.models import Category, Product

admin.site.register(Product)
admin.site.register(Category)