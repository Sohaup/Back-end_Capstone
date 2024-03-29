from django import forms
from .models import Reservations

class Reservation_Form(forms.ModelForm):
    reserv = [['1','1pm'],['2','2pm'],['3','3pm'],['4','4pm'],['5','5pm']]
    class Meta:
        model =  Reservations
        fields = ['name','date','time']
    

