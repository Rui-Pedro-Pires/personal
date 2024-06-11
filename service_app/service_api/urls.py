from django.urls import path, include
from .views import (
    ClientApiView,
    VehicleApiView,
    ServiceApiView,
    EventApiView,
)

urlpatterns = [
    path('client', ClientApiView.as_view()),
    path('vehicle', VehicleApiView.as_view()),
    path('service', ServiceApiView.as_view()),
    path('event', EventApiView.as_view()),
]