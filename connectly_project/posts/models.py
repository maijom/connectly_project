from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)  # User's unique username
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the user was created


    def __str__(self):
                return self.username