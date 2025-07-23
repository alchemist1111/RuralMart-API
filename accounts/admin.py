from django.contrib import admin
from .models import UserProfile, CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    # Define the fields to display in the admin interface
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'is_active', 'is_staff')
    
    # Search functionality
    search_fields = ('email', 'first_name', 'last_name', 'email')
    
    # List filter
    list_filter = ('is_active', 'is_staff', 'roles', 'date_joined', 'last_login')
    
    # Options for ordering
    ordering = ('-date_joined',)
    
# Register UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    # Fields to display in the admin interface
    list_display = ('user', 'address', 'profile_picture', 'created_at', 'updated_at')
    
    # Search fields 
    search_fields = ('user_email', 'user__first_name', 'user__last_name', 'address') 
    
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)    
