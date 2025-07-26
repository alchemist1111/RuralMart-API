from django.contrib import admin
from .models import Category, Product

# Category model registration with admin site
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Products model registration with admin site
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category')
    search_fields = ('name', 'price')
    list_filter = ('category', 'created_at', 'updated_at')
