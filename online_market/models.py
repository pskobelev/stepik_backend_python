from django.db import models


# Create your models here.
class Good(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.price}"


class Token(models.Model):
    token_id = models.CharField(max_length=36)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"token: {self.created_at}"
