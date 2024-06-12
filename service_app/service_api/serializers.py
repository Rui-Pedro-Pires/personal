from rest_framework import serializers
from .models import (
    Client,
    Vehicle,
    Service,
    Event,
    Technician,
    InfoService,
    Tipology,
)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.CharField(source='vehicle.plate', read_only=True)
    class Meta:
        model = Event
        fields = ['id', 'vehicle_plate', 'obs', 'entry_date', 'start_hour', 'end_date', 'end_hour']

class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = "__all__"

class InfoServiceSerializer(serializers.ModelSerializer):
    plate = serializers.CharField(source='idEvent.vehicle.plate', read_only=True)
    service = serializers.CharField(source='idService.name', read_only=True)
    technician = serializers.CharField(source='idTechnician.name', read_only=True)
    class Meta:
        model = InfoService
        fields = ['id', 'plate', 'service', 'technician', 'onGoing', 'startDate', 'finishDate', 'totalTime']

class TipologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipology
        fields = "__all__"

class HomeSerializer(serializers.ModelSerializer):
    plate = serializers.CharField(source='idEvent.vehicle.plate', read_only=True)

    class Meta:
        model = InfoService
        fields = []