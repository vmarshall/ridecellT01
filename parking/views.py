from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework_gis.filters import DistanceToPointFilter

from parking.models import ParkingSpot
from parking.serializer import UserSerializer, ParkingSpotSerializer
from rest_framework import filters

from rest_framework import generics
from django.core.serializers import serialize

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ParkingSpotViewSet(viewsets.ModelViewSet):

    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    distance_filter_field = 'point'
    filter_backends = (DistanceToPointFilter,)
    distance_filter_convert_meters = True

def index(request):
    context = {}
    return render(request, 'parking/index.html', context)
