from .serializer import HolidaySerializer
from rest_framework import viewsets
from .models import Holidays
# Create your views here.

class HolidayViewSet(viewsets.ModelViewSet):
    queryset= Holidays.objects.all()
    serializer_class=HolidaySerializer