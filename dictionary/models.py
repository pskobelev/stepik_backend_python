from django.db import models


class Words(models.Model):
    """Words model"""
    word = models.CharField(max_length=100)
    description = models.TextField()


