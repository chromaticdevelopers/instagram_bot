from django.db import models
from django.utils import timezone

class UserStatus(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255)
    last_login_timestamp = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return f"User {self.user_id} - Status: {self.status}"
    def save(self, *args, **kwargs):
        # Update last_login_timestamp to current Unix timestamp if it's a new instance
        if not self.pk:
            self.last_login_timestamp = int(timezone.now().timestamp())
        super().save(*args, **kwargs)

class Menu(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    image_url = models.URLField()
    main_menu = models.BooleanField(default=False)
    successor_of = models.ForeignKey('OptionsMenu', on_delete=models.CASCADE, null=True, blank=True, unique=True, related_name='successor_of')

    def __str__(self):
        return self.title
class OptionsMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    payload = models.CharField(max_length=255)
    TYPE_CHOICES = [
        ('URL', 'URL'),
        ('BUTTON', 'Button'),
    ]
    type = models.CharField(max_length=6, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title