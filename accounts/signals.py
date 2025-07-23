from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import UserProfile, CustomUser

# Automatically create or update UserProfile when CustomUser is saved
@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    try:
        if created:
            UserProfile.objects.create(user=instance)
    except Exception as e:
        print(f"Error creating UserProfile for {instance}: {e}")
        
# Automatically delete UserProfile when CustomUser is deleted
@receiver(post_delete, sender=CustomUser)
def delete_user_profile(sender, instance, **kwargs):
    try:
        instance.userprofile.delete()
    except UserProfile.DoesNotExist:
        print(f"UserProfile for {instance} does not exist, nothing to delete.") 