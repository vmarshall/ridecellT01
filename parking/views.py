from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework_gis.filters import DistanceToPointFilter

from parking.models import ParkingSpot
from parking.serializer import UserSerializer, GroupSerializer, ParkingSpotSerializer
from rest_framework import filters

from rest_framework import generics

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ParkingSpotViewSet(viewsets.ModelViewSet):


    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('label', 'radius')

# class SearchList(generics.ListAPIView):
#     serializer_class = ParkingSpotSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         car = self.request.user
#         current_loc = self.request.user.location
#         available_spots = ParkingSpot.objects.filter(point__distance_lte=(current_loc, self.search_radius))
#         return ParkingSpot.objects.filter(owner=user)
#
#     def find_parking(self):
#         current_loc = self.location
#         available_spots =  ParkingSpot.objects.filter(point__distance_lte=(current_loc, self.search_radius))
#         pass


class SearchByRadiusList(ListAPIView):

    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    distance_filter_field = 'geometry'
    filter_backends = (DistanceToPointFilter, )
    bbox_filter_include_overlapping = True # Optional




def index(request):
    context = {}
    return render(request, 'parking/index.html', context)
