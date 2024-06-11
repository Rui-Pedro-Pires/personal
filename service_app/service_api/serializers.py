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
    class Meta:
        model = Event
        fields = "__all__"

class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = "__all__"

class InfoServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoService
        fields = "__all__"

class TipologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipology
        fields = "__all__"