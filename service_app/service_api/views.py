from django.shortcuts import render, get_object_or_404
from django.utils import timezone
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
    TipologySerializer,
    InfoServiceSerializer,
)
# Create your views here.

class ClientApiView(APIView):

    def get(self, request, *args, **kwargs):
        clients = Client.objects.all()
        serielizer = ClientSerializer(clients, many=True)
        return Response(serielizer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        try:
            client = get_object_or_404(Client, id=kwargs['id'])
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            client = get_object_or_404(Client, id=kwargs['id'])
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)

class VehicleApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            if 'plate' in kwargs:
                vehicle = get_object_or_404(Vehicle, plate=kwargs['plate'])
                serializer = VehicleSerializer(vehicle)
            else:
                vehicle = Vehicle.objects.all()
                serializer = VehicleSerializer(vehicle, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        client_name = request.data.get('client')
        try:
            client = get_object_or_404(Client, name=client_name)
        except:
            data = {
                "name" : request.data.get('client'),
                "telem" : request.data.get('telem'),
                "email" : request.data.get('email')
            }
            serializer = ClientSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                try:
                    client = get_object_or_404(Client, name=client_name)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
        data = {
            "client": client.id,
            "plate": request.data.get('plate'),
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
    
    def delete(self, request, *args, **kwargs):
        vehicle = get_object_or_404(Vehicle, id=kwargs['id'])
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ServiceApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            if 'type' in kwargs:
                services = get_object_or_404(Service, type=kwargs['type'])
                serializer = ServiceSerializer(services)
            else:
                services = Service.objects.all()
                serializer = ServiceSerializer(services, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, *args, **kwargs):
        tipology_name = request.data.get('type')
        try:
            tipology = get_object_or_404(Tipology, type=tipology_name)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        data = {
            "idType":  tipology.id,
            "name": request.data.get('name'),
            "time": request.data.get('time'),
            "description": request.data.get('description')
        }
        serializer = ServiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class CreateServiceApiView(APIView):

    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        plate = request.data.get('plate')
        services = request.data.get('services')
        try:
            vehicle = get_object_or_404(Vehicle, plate=plate)
        except:
            client_data = {
                "name": request.data.get('name'),
                "telem": request.data.get('telem'),
                "email": request.data.get('email')
            }
            client_serializer = ClientSerializer(data=client_data)
            if client_serializer.is_valid():
                client_serializer.save()
            else:
                return Response(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            vehicle_data = {
                "client": client_serializer.instance.id,
                "plate": request.data.get('plate'),
                "brand": request.data.get('brand'),
                "model": request.data.get('model'),
                "km": request.data.get('km'),
                "year": request.data.get('year')
            }
            vehicle_serializer = VehicleSerializer(data=vehicle_data)
            if vehicle_serializer.is_valid():
                vehicle_serializer.save()
            else:
                return Response(vehicle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        data = {
            'vehicle': vehicle.id,
            'entry_date': request.data.get('entry_date'),
            'start_hour': request.data.get('entry_hour'),
            'end_date': request.data.get('end_date'),
            'end_hour': request.data.get('end_hour'),
        }
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        event_id = serializer.instance.id
        for service in services:
            try:
                service_obj = get_object_or_404(Service, name=service)
                data = {
                    'idEvent': event_id,
                    'idService': service_obj.id,
                }
                serializer = InfoServiceSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)

class TechnicianApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        technicians = Technician.objects.all()
        serializer = TechnicianSerializer(technicians, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = TechnicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            technician = get_object_or_404(id=kwargs['id'])
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        technician.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TipologyApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        serializer = TipologySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InfoServiceApiView(APIView):

    def get(self, request, *args, **kwargs):
        infoService = InfoService.objects.all()
        serializer = InfoServiceSerializer(infoService, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, *args, **kwargs):
        if 'id' in kwargs:
            try:
                infoService = get_object_or_404(InfoService, id=kwargs['id'])
            except:
                return Response(status=status.HTTP_200_OK)
            name = request.data.get('technician')
            ongoing = request.data.get('onGoing')
            if not name:
                if ongoing and ongoing == "True":
                    data = {
                        "onGoing": "True",
                        "startDate": timezone.now()
                    }
                    serializer = InfoServiceSerializer(infoService, data=data, partial=True)
                else:
                    serializer = InfoServiceSerializer(infoService, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            try:
                technician = get_object_or_404(Technician, name=name)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            if not ongoing:
                ongoing = False
                data = {
                    "idTechnician": technician.id,
                    "onGoing": ongoing,
                }
            elif ongoing == "True":
                data = {
                    "idTechnician": technician.id,
                    "onGoing": ongoing,
                    "startDate": timezone.now()
                }
            serializer = InfoServiceSerializer(infoService, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class HomeApiView(APIView):
#     def get(self, request, *args, **kwargs):
