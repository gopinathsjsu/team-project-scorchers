from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from . import models
from django.forms import modelformset_factory
from django import forms
from django.core import management
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Q
from .forms import AddFlight, FlightOptions

def home(request):
    return render(request, 'airport_system/home.html')

def flights_options(request):
    if request.method == 'POST':
        hours = request.POST['hours']
        #print('Hours in flight_options', hours)
        return redirect('flights', hours)
    form = FlightOptions()
    context = {'form' : form}
    return render(request, 'airport_system/flights_options.html', context)

def airport_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.airportemp:
                login(request, user)
                return redirect('airport_edit_options')
        else:
            message = 'Error: Please check the details and login again!'
            form = AuthenticationForm(request)
            context = {'form' : form, 'message' : message}
            #context = {'message' : message}
            return render(request, 'airport_system/airport_login.html', context)

    form = AuthenticationForm(request)
    context = {'form' : form}

    return render(request, 'airport_system/airport_login.html', context)

def airline_login(request):
    airline_objs = models.Airline.objects.all()
    airline_list = []
    for i in airline_objs:
        airline_list.append(i.name)
    #print(airline_list)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        airline = request.POST['airline']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.airlineemp and user.airlineemp.airline.name == airline:
                login(request, user)
                #print('airline in airline_login:', airline)
                return redirect('airline_edit_options')

        else:
            message = 'Error: Please check the details and login again!'
            form = AuthenticationForm(request)
            context = {'form' : form, 'message' : message, 'airline_list' : airline_list}
            return render(request, 'airport_system/airline_login.html', context)

    form = AuthenticationForm(request)
    context = {'form' : form, 'airline_list' : airline_list}
    return render(request, 'airport_system/airline_login.html', context)

def flights(request, hours):
    #print('Hours:', hours)
    details = models.Flight.objects.filter(Q(schedule_time__gt = timezone.now()) & Q(schedule_time__lt=timezone.now()+timedelta(hours=hours))).order_by('status')
    #arr_ = models.flight.objects.filter(status='Arriving')
    #dep_ = models.flight.objects.filter(status='Departure')
    context = {'details' : details, 'hours': hours }
    return render(request, 'airport_system/flights.html', context)

def airline_update_flight(request):
    FlightFormSet = modelformset_factory(models.Flight, fields=('number','schedule_time'), extra=0, widgets={'number': forms.HiddenInput(), 'schedule_time' : forms.TextInput(attrs={'type':'datetime-local'})})
    if request.method == 'POST':
        formset = FlightFormSet(request.POST, queryset=models.Flight.objects.filter(airline=request.user.airlineemp.airline))
        #print(formset)
        if formset.is_valid():
            #print('valid')
            formset.save()
            management.call_command('updategates')
            return redirect('airline_update_flight')
    else:
        formset = FlightFormSet(queryset=models.Flight.objects.filter(airline=request.user.airlineemp.airline))


    #flightdets = models.Flight.objects.filter(airline=request.user.airlineemp.airline)
    context = {'formset' : formset}
    return render(request, 'airport_system/airline_update_flight.html', context)

def airline_add_flight(request):
    if request.method == 'POST':
        form = AddFlight(request.POST)
        if form.is_valid():
            number = request.POST['number']
            airline = request.user.airlineemp.airline
            status = request.POST['status']
            schedule = request.POST['schedule']
            
            obj = models.Flight(number=number,airline=airline,status=status,schedule_time=schedule)
            obj.save()
            print('record saved')
            return redirect('airline_add_flight')

    else:
        form = AddFlight()
    
    context={'form' : form}
    return render(request, 'airport_system/airline_add_flight.html', context)

def airport_edit_gates(request):
    flightobjs = models.Flight.objects.all()
    gatef_list = []
    for obj in flightobjs:
        gatef_list.append(obj.gate)

    FlightFormSet = modelformset_factory(models.Gate, fields=('id', 'active'), extra=0, widgets={'id':forms.HiddenInput(), 'active' : forms.Select(choices=(('True',bool(1)),('False',bool(0))))})

    if request.method == 'POST':
        print('post method')
        print(FlightFormSet)
        formset = FlightFormSet(request.POST, queryset=models.Gate.objects.exclude(label__in = gatef_list))
        print(formset)
        if formset.is_valid():
            print('valid')
            formset.save()
            management.call_command('updategates')
            return redirect('airport_edit_gates')

        print(formset)
    else:
        formset = FlightFormSet(queryset=models.Gate.objects.exclude(label__in = gatef_list))

    context = {'formset' : formset}
    return render(request, 'airport_system/airport_edit_gates.html', context)

def airport_edit_options(request):
    return render(request, 'airport_system/airport_edit_options.html')

def airport_edit_baggage_old(request):
    arriv_flights = models.Flight.objects.filter(status='Arriving')
    bag = []
    for obj in arriv_flights:
        bag.append(obj.baggage_claim)
    choices=[]
    avail_bag = models.BaggageClaim.objects.exclude(label__in = bag)
    for obj in avail_bag:
        choices.append((obj.label,obj.label))

    FlightFormSet = modelformset_factory(models.Flight, fields={'number', 'baggage_claim'}, extra=0, widgets={'number':forms.HiddenInput(), 'baggage_claim':forms.Select(choices=tuple(choices))})

    if request.method == 'POST':
        formset = FlightFormSet(request.POST, queryset=models.Flight.objects.filter(status='Arriving'))
        if formset.is_valid():
            print('valid formset')
            formset.save()
            return redirect('airport_edit_baggage')
    else:
        formset = FlightFormSet(queryset=models.Flight.objects.filter(status='Arriving', schedule_time__lt=timezone.now()+timedelta(hours=2)))
    
    context = {'formset' : formset}

    return render(request, 'airport_system/airport_edit_baggage.html', context)

def airport_edit_baggage(request):
    arriv_flights = models.Flight.objects.filter(status='Arriving')
    bag = []
    for obj in arriv_flights:
        bag.append(obj.baggage_claim)
    choices=[]
    avail_bag = models.BaggageClaim.objects.exclude(label__in = bag)
    for obj in avail_bag:
        choices.append((obj.label,obj.label))

    FlightFormSet = modelformset_factory(models.Flight, fields={'number', 'baggage_claim'}, extra=0, widgets={'number':forms.HiddenInput(), 'baggage_claim':forms.Select(choices=tuple(choices))})

    if request.method == 'POST':
        formset = FlightFormSet(request.POST, queryset=models.Flight.objects.filter((Q(schedule_time__gt = timezone.now()) & Q(schedule_time__lt=timezone.now()+timedelta(hours=2))), status='Arriving'))
        if formset.is_valid():
            print('valid formset')
            formset.save()
            return redirect('airport_edit_baggage')
        else:
            message = 'Error:Please enter unique values!'
            formset = FlightFormSet(queryset=models.Flight.objects.filter((Q(schedule_time__gt = timezone.now()) & Q(schedule_time__lt=timezone.now()+timedelta(hours=2))), status='Arriving'))
            context = {'message': message,'formset':formset}
            return render(request, 'airport_system/airport_edit_baggage.html', context)
    else:
        formset = FlightFormSet(queryset=models.Flight.objects.filter((Q(schedule_time__gt = timezone.now()) & Q(schedule_time__lt=timezone.now()+timedelta(hours=2))), status='Arriving'))
    
    context = {'formset' : formset}

    return render(request, 'airport_system/airport_edit_baggage.html', context)

def airline_edit_options(request):
    return render(request, 'airport_system/airline_edit_options.html')



