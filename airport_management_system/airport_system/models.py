from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone

class AirportEmp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class AirlineEmp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    airline = models.ForeignKey('Airline', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username


class Flight(models.Model):
    number = models.CharField(max_length=6, primary_key=True, default='A1234')
    status = models.CharField(max_length=30)
    gate = models.ForeignKey('Gate', on_delete=models.CASCADE, null=True, blank=True)
    airline = models.ForeignKey('Airline', on_delete=models.CASCADE)
    schedule_time = models.DateTimeField()
    baggage_claim = models.ForeignKey('BaggageClaim', null=True, blank=True, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.number


class Gate(models.Model):
    label = models.CharField(max_length=3)
    terminal = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.label

class Airline(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class BaggageClaim(models.Model):
    label = models.CharField(max_length=4)

    def __str__(self):
        return self.label







