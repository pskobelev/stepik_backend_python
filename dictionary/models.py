from django.db import models


class Words(models.Model):
    word = models.CharField(max_length=100)
    description = models.TextField()
