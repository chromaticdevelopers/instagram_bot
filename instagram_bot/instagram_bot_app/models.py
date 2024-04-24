from django.db import models

# Create your models here.
class UserStatus(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"User {self.user_id} - Status: {self.status}"