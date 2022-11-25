from django.core.management.base import BaseCommand, CommandError
from airport_system.models import Flight, Gate
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Q

class Command(BaseCommand):

    def handle(self, *args, **options):
        Flight.objects.filter(Q(schedule_time__lt = timezone.now()) | Q(schedule_time__gt=timezone.now()+timedelta(hours=2))).update(gate=None)
        flights = Flight.objects.filter(gate=None, schedule_time__range=(timezone.now(), timezone.now()+timedelta(hours=2)))
        #avail_gates = Gate.objects.filter(active=True)
        #all_flights = Flight.objects.all()
        
        avail_gates = Gate.objects.filter(flight=None, active=True).order_by('?').all()
        for flight,gate in zip(flights,avail_gates):
            flight.gate = gate
            flight.save()
            
        #if self.schedule_time < timezone.now() - timedelta(hours=2):
         #   self.gate = None
        print(avail_gates)


        self.stdout.write(self.style.SUCCESS('Command test'))