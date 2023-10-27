from django.db import models


class Words(models.Model):
    word = models.CharField(max_length=100)
    description = models.TextField()


class Fuel(models.Model):
    fuel = models.CharField(max_length=100)
    cost = models.FloatField(default=0)
    distance = models.IntegerField(default=0)
    data_fuel = models.DateField(auto_now_add=True)
    date_fuel = models.DateTimeField(auto_now_add=True)
    fuel_consumption = models.FloatField(blank=True, default=0)

    def __str__(self):
        return f'Заправка на {self.fuel} литров, на сумму {self.cost} руб, дистанция {self.distance} км'
