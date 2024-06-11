from django.db import models
from datetime import datetime 

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=180, null=True)
    telem = models.IntegerField(blank=True)
    email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    plate = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    km = models.IntegerField()
    year = models.DateField(null=True)

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
    entry_date = models.DateField(default=datetime.now, null= False)
    start_hour = models.DateTimeField(default=datetime.now, null=False)
    end_date = models.DateField(default=datetime.now, null=False)
    end_hour = models.DateTimeField(default=datetime.now, null=False)

    def __str__(self):
        return self.service.name

class Technician(models.Model):
    name = models.CharField(max_length=180, null=True)

    def __str__(self):
        return self.name

class InfoService(models.Model):
    idEvent = models.ForeignKey(Event, on_delete=models.CASCADE)
    idService = models.ForeignKey(Service, on_delete=models.CASCADE)
    idTechnician = models.ForeignKey(Technician, on_delete=models.CASCADE, blank=True)
    onGoing = models.BooleanField(default=False)
    startDate = models.DateField(default=datetime.now)
    finishDate = models.DateField(default=datetime.now)
    totalTime = models.DateField(default=datetime.now)

    def __str__(self):
        return self.id
