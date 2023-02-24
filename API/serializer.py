from rest_framework import serializers
from .models import Holidays

class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model= Holidays
        fields= '__all__'
