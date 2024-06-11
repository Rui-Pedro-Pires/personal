from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import (
    Client,
    Vehicle,
    Service,
    Event,
    Tipology,
    Technician,
    InfoService,
)
from .serializers import (
    ClientSerializer,
    VehicleSerializer,
    ServiceSerializer,
    EventSerializer,
    TechnicianSerializer,
    InfoServiceSerializer,
)
# Create your views here.

class ClientApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        clients = Client.objects.all()
        serielizer = ClientSerializer(clients, many=True)
        return Response(serielizer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'telem': request.data.get('telem'),
            'email': request.data.get('email')
        }
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VehicleApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        client_name = request.data.get('cliente')
        client_id = Client.objects.filter(nome=client_name).values_list('id', flat=True).first()

        if not client_id:
            return Response({"detail": "Client not found."}, status=status.HTTP_400_BAD_REQUEST)
        
        data = {
            "client": client_id,
            "palte": request.data.get('plate'),
            "brand": request.data.get('brand'),
            "model": request.data.get('model'),
            "km": request.data.get('km'),
            "year": request.data.get('year')
        }
        serializer = VehicleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        tipology_name = request.data.get('typology')
        tipology_id = Tipology.objects.filter(name=tipology_name).values_list('id', flat=True).first()
        data = {
            "idType":  tipology_id,
            "name": request.data.get('name'),
            "time": request.data.get('time'),
            "description": request.data.get('description')
        }
        serializer = ServiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class EventApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        plate = request.data.get('vehicle')
        plate_id = Vehicle.objects.filter(matricula=plate).values_list('id', flat=True).first()
        data = {
            'vehicle': plate_id,
            'entry_date': request.data.get('data_entrada'),
            'start_hour': request.data.get('hora_entrada'),
            'end_date': request.data.get('data_saida'),
            'end_hour': request.data.get('hora_saida'),
        }
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)