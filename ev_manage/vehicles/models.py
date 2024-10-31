# Create your models here.
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('scooter', 'Electric Scooter'),
        ('bike', 'Electric Bike'),
    ]
    type = models.CharField(max_length=50, choices=VEHICLE_TYPES)
    battery_level = models.IntegerField(default=100)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    is_available = models.BooleanField(default=True)
    is_defective = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.type} - {self.id}"
