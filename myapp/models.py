

# Create your models here.
from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    review = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
    


class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"    