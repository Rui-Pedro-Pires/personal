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
            'nome': request.data.get('nome'),
            'telemovel': request.data.get('telemovel'),
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
            "clientes": client_id,
            "matricula": request.data.get('matricula'),
            "marca": request.data.get('marca'),
            "modelo": request.data.get('modelo'),
            "km": request.data.get('km'),
            "ano": request.data.get('ano')
        }

        serializer = veiculosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        _servicos = servicos.objects.all()
        serializer = servicosSerializer(_servicos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            "nome": request.data.get('nome'),
            "tempo": request.data.get('tempo'),
            "obs": request.data.get('obs') 
        }
        serializer = servicosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class EventApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        _servicos_total = servicos_total.objects.all()
        serializer = servicos_totalSerializer(_servicos_total, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        matricula = request.data.get('veiculo')
        service_nome = request.data.get('service')

        matricula_id = veiculos.objects.filter(matricula=matricula).values_list('id', flat=True).first()
        service_id = servicos.objects.filter(nome=service_nome).values_list('id', flat=True).first()
        data = {
            'veiculos': matricula_id,
            'servicos': service_id,
            'data_entrada': request.data.get('data_entrada'),
            'hora_entrada': request.data.get('hora_entrada'),
            'data_saida': request.data.get('data_saida'),
            'hora_saida': request.data.get('hora_saida'),
            'descricao': request.data.get('descricao')
        }
        serializer = servicos_totalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)