from django.urls import path, include
from .views import (
    ClientApiView,
    VehicleApiView,
    ServiceApiView,
    CreateServiceApiView,
    TechnicianApiView,
    TipologyApiView,
    InfoServiceApiView,
)

urlpatterns = [
    path('client', ClientApiView.as_view()),
    path('client/<int:id>', ClientApiView.as_view()),
    path('vehicle', VehicleApiView.as_view()),
    path('vehicle/<int:id>', VehicleApiView.as_view()),
    path('vehicle/<str:plate>', VehicleApiView.as_view()),
    path('service', ServiceApiView.as_view()),
    path('service/<str:type>', ServiceApiView.as_view()),
    path('create', CreateServiceApiView.as_view()),
    path('technician', TechnicianApiView.as_view()),
    path('technician/<int:id>', TechnicianApiView.as_view()),
    path('tipology', TipologyApiView.as_view()),
    path('infoservice', InfoServiceApiView.as_view()),
    path('infoservice/<int:id>', InfoServiceApiView.as_view()),
]