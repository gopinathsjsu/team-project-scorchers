from django import forms

class DateTimeInput(forms.DateTimeInput):
    input_type='datetime-local'

class AddFlight(forms.Form):
    number = forms.CharField(max_length=30)
    status = forms.ChoiceField(choices=(('Arrival','Arrival'), ('Departure','Departure')))
    schedule = forms.DateTimeField(widget=DateTimeInput)
    
class FlightOptions(forms.Form):
    hours = forms.IntegerField(max_value=8, min_value=1)
