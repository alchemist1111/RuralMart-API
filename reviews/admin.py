from django.contrib import admin
from .models import Review

# Register review model with the admin site
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'comment', 'created_at')
    search_fields = ('user', 'product')
    list_filter = ('rating', 'created_at')
