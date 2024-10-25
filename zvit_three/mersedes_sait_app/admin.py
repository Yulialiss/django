from django.contrib import admin
from .models import Product, PersonalData, User

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'car_model', 'car_type', 'color')
    search_fields = ('name', 'car_model', 'car_type', 'color')

admin.site.register(Product)
admin.site.register(PersonalData)
admin.site.register(User)