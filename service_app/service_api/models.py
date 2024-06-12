from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=180, null=True, unique=True)
    telem = models.IntegerField(blank=True, unique=True)
    email = models.CharField(max_length=50, null=True, unique=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    plate = models.CharField(max_length=20, unique=True)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    km = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return self.plate

class Tipology(models.Model):
    type = models.CharField(max_length=180, null=False)

    def __str__(self):
        return self.type

class Service(models.Model):
    idType = models.ForeignKey(Tipology, on_delete=models.CASCADE)
    name = models.CharField(max_length=180, null=True)
    time = models.IntegerField(null=True)
    description = models.CharField(max_length=180, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    obs = models.CharField(max_length=256, null=True)
    entry_date = models.DateField(default=datetime.now, null= False)
    start_hour = models.TimeField(default=timezone.now, null=False)
    end_date = models.DateField(default=datetime.now, null=False)
    end_hour = models.TimeField(default=timezone.now, null=False)

    def __str__(self):
        return str(self.id) + "from plate: " +  self.vehicle.plate

class Technician(models.Model):
    name = models.CharField(max_length=180, null=True)

    def __str__(self):
        return self.name

class InfoService(models.Model):
    idEvent = models.ForeignKey(Event, on_delete=models.CASCADE)
    idService = models.ForeignKey(Service, on_delete=models.CASCADE)
    idTechnician = models.ForeignKey(Technician, on_delete=models.CASCADE, blank=True, null=True)
    onGoing = models.BooleanField(default=False, blank=True)
    startDate = models.DateTimeField(null=True, blank=True)
    finishDate = models.DateTimeField(null=True, blank=True)
    totalTime = models.DurationField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + " is on going:" + str(self.onGoing)
