from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeoModelSerializer

from parking.models import ParkingSpot

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class LocationSerializer(GeoModelSerializer):

    class Meta:
        model = ParkingSpot
        geo_field = "point"
        fields = ("point",)


class ParkingSpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = ('id', 'rcpid', 'owner', 'reserved', 'label', "point")

