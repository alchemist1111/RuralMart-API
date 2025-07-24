from django.db import models
from accounts.models import CustomUser

# Class to represent audit logs
class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
        ('view', 'View'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='audit_logs')
    action = models.CharField(max_length=255, choices=ACTION_CHOICES)
    model_name = models.CharField(max_length=255)
    model_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.action} - {self.model_name} (ID: {self.model_id}) at {self.timestamp}"
