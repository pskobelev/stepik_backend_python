from django.db import models
from django.forms import ModelForm


# Create your models here.
class Fuel(models.Model):
    fuel = models.CharField(max_length=100)
    cost = models.FloatField(default=0)
    distance = models.IntegerField(default=0)

    date_fuel = models.DateTimeField(auto_now_add=True)
    fuel_consumption = models.FloatField(blank=True, default=0)

    def __str__(self):
        return f"Заправка {self.cost} руб."


class MyFuelForm(ModelForm):
    class Meta:
        model = Fuel
        fields = ["fuel", "distance", "cost"]
