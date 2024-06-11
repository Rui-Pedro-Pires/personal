from django.urls import path, include
from .views import (
    ClientApiView,
    VehicleApiView,
    ServiceApiView,
    EventApiView,
)

urlpatterns = [
    path('servicos', servicosApiView.as_view()),
    path('clientes', clienteApiView.as_view()),
    path('veiculos', veiculosApiView.as_view()),
    path('adicionar', servicos_totalApiView.as_view()),
]