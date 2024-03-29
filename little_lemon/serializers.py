from rest_framework import serializers
from .models import Reservations

class Reservations_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Reservations
        fields = '__all__'