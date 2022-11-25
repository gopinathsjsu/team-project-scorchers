from django.contrib import admin
from . import models

admin.site.register(models.AirportEmp)
admin.site.register(models.AirlineEmp)
admin.site.register(models.Flight)
admin.site.register(models.Gate)
admin.site.register(models.Airline)
admin.site.register(models.BaggageClaim)
