from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('airline_login/', views.airline_login, name='airline_login'),
    path('airport_login/', views.airport_login, name='airport_login'),
    path('flights_options/', views.flights_options, name='flights_options'),
    path('flights/<int:hours>', views.flights, name='flights'),
    path('airline_edit_options/', views.airline_edit_options, name='airline_edit_options'),
    path('airline_add_flight/', views.airline_add_flight, name='airline_add_flight'),
    path('airline_update_flight/', views.airline_update_flight, name='airline_update_flight'),
    path('airport_edit_gates/', views.airport_edit_gates, name='airport_edit_gates'),
    path('airport_edit_baggage/', views.airport_edit_baggage, name='airport_edit_baggage'),
    path('airport_edit_options/', views.airport_edit_options, name='airport_edit_options'),

]