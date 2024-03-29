from django.shortcuts import render,redirect
from .models import Reservations
from .forms import Reservation_Form
from django.http import HttpResponse
from .serializers import Reservations_Serializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def Main_View(request):
    form = Reservation_Form
    reservations = Reservations.objects.raw('SELECT id , name , time FROM little_lemon_reservations') 
    context = {'form':form , 'data':reservations}
    if request.method == 'POST':
        form = Reservation_Form(request.POST)
        if form.is_valid():
             form.save()
             return HttpResponse('Success')
        else:  
            return HttpResponse('Failed')  
    return render(request,'main.html',context)       


def Success_View(request):
    return HttpResponse('success')


class Reservations_View(generics.CreateAPIView):
    queryset=Reservations.objects.all()
    serializer_class=Reservations_Serializer

@api_view()  
def Show_Reservations(request):  
       reservations = Reservations.objects.all()
       date = request.GET.get('date')
       if date:
        reservations = reservations.filter(date__contains=date)
       else: 
         reservations=Reservations.objects.all()
       return Response(reservations.values())