from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from . import models

def home(request):
    return render(request, 'airport_system/home.html')

def airport_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.airportemp:
                login(request, user)
                return redirect('airport_edit')

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
                request.session['airline'] = airline
                login(request, user)
                #print('airline in airline_login:', airline)
                return redirect('airline_edit', airline=airline)

        else:
            message = 'Error: Please check the details and login again!'
            form = AuthenticationForm(request)
            context = {'form' : form, 'message' : message, 'airline_list' : airline_list}
            #context = {'message' : message}
            return render(request, 'airport_system/airline_login.html', context)

    form = AuthenticationForm(request)
    context = {'form' : form, 'airline_list' : airline_list}
    return render(request, 'airport_system/airline_login.html', context)

def flights(request):
    details = models.Flight.objects.all()
    context = {'details' : details}
    return render(request, 'airport_system/flights.html', context)

def airline_edit(request, airline):
    #print(request.session['airline'])
    if request.method == 'POST':
        print(airline)
        flightdets = models.Flight.objects.get(airline=airline)
        context = {'flightdets' : flightdets}
        return render(request, 'airport_system/airline_edit.html', context)

def airport_edit(request):
    return render(request, 'airport_system/airport_edit.html')



