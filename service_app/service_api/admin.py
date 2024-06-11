from django.contrib import admin
from .models import (
    Client,
    Vehicle,
    Service,
    Event,
    Tipology,
    Technician,
    InfoService,
)

admin.site.register(Client)
admin.site.register(Vehicle)
admin.site.register(Service)
admin.site.register(Event)
admin.site.register(Tipology)
admin.site.register(Technician)
admin.site.register(InfoService)
# Register your models here.
