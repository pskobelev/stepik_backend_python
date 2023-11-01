from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    """Note model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note at {self.user}"
