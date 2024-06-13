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
    InfoServicePutSerializer,
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
        client = get_object_or_404(Client, id=kwargs['id'])
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        client = get_object_or_404(Client, id=kwargs['id'])
        return Response(status=status.HTTP_204_NO_CONTENT)

class VehicleApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if 'plate' in kwargs:
            vehicle = get_object_or_404(Vehicle, plate=kwargs['plate'])
            serializer = VehicleSerializer(vehicle)
        else:
            vehicle = Vehicle.objects.all()
            serializer = VehicleSerializer(vehicle, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
                client = get_object_or_404(Client, name=client_name)
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
        if 'type' in kwargs:
            services = get_object_or_404(Service, type=kwargs['type'])
            serializer = ServiceSerializer(services)
        else:
            services = Service.objects.all()
            serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        tipology_name = request.data.get('type')
        tipology = get_object_or_404(Tipology, type=tipology_name)
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
        technician = get_object_or_404(id=kwargs['id'])
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
        if 'id' in kwargs:
            infoservice = InfoService.objects.filter(idEvent=kwargs['id'])
            serializer = InfoServiceSerializer(infoservice, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        infoService = InfoService.objects.all()
        serializer = InfoServiceSerializer(infoService, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, *args, **kwargs):
        if 'id' in kwargs:
            infoService = get_object_or_404(InfoService, id=kwargs['id'])
            name = request.data.get('technician')
            ongoing = request.data.get('onGoing')
            if not name:
                if ongoing and ongoing == "2":
                    data = {
                        "onGoing": ongoing,
                        "startDate": timezone.now()
                    }
                    serializer = InfoServiceSerializer(infoService, data=data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_200_OK)
                elif ongoing and ongoing == "3":
                    totalTime = timezone.now() - infoService.startDate
                    data = {
                        "onGoing": ongoing,
                        "finishDate": timezone.now(),
                        "totalTime": totalTime
                    }
                    serializer = InfoServiceSerializer(infoService, data=data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            technician = get_object_or_404(Technician, name=name)
            if technician:
                print(technician)
                print(infoService.idTechnician)
                data = {
                    "idTechnician": technician.id,
                }
                serializer = InfoServicePutSerializer(infoService, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    print(serializer.data)
                    return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
