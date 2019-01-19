import uuid

from django.contrib.gis.geos import Point
from django.db import models
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from django.contrib.auth.models import User
import factory.django, random
from factory.fuzzy import BaseFuzzyAttribute

from ridecellT01 import settings
from django.contrib.gis.db import models as geo_models
from django.contrib.gis.geos import Point

# class RidecellUser(AbstractUser):
#     pass





class Car(models.Model):

    driver = models.ForeignKey(User,  on_delete = models.CASCADE, blank=True, null=True, help_text="Current car")
    location = geo_models.PointField(null=True, blank=True)
    search_radius = models.FloatField(default=2.0)

    def __str__(self):
        return "%s - %s" % (self.driver.username ,self.location)


class ParkingSpot(models.Model):

    rcpid = models.UUIDField(default=uuid.uuid4, editable=False)

    owner = models.ForeignKey(User, on_delete = models.CASCADE,blank=True,null=True, help_text="Current owner " )
    available = models.BooleanField(default=False) # should probably turn this into an enum of some sort of 'state'

    label = models.CharField(default='unidentified', max_length=256, help_text="Human readable label")

    lon = models.FloatField(default=37.7749)
    lat = models.FloatField(default=122.4194)

    location = geo_models.PointField(null=True, blank=True)

    created_timestamp = CreationDateTimeField()
    modified_timestamp = ModificationDateTimeField()

    def __str__(self):
        return "%s - %s" % (self.label, self.location)


