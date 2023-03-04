from .serializer import HolidaySerializer
from rest_framework import viewsets
from .models import Holidays
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class HolidayViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset= Holidays.objects.all()
    serializer_class=HolidaySerializer
    