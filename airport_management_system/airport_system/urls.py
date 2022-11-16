from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('airline_login/', views.airline_login, name='airline_login'),
    path('airport_login/', views.airport_login, name='airport_login'),
    path('flights/', views.flights, name='flights'),
    path('airline_edit/<str:airline>', views.airline_edit, name='airline_edit'),
    path('airport_edit/', views.airport_edit, name='airport_edit'),

]