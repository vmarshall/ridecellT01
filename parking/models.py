import uuid
from django.db import models
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geo_models
from django.contrib.gis.geos import Point


class ParkingSpot(models.Model):

    rcpid = models.UUIDField(default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete = models.CASCADE,blank=True,null=True, help_text="Owner of the reservation" )
    reserved = models.BooleanField(default=False) # should probably turn this into an enum of some sort of 'state'

    label = models.CharField(default='unidentified', max_length=256, help_text="Human readable label")

    location = Point(-122.4194, 37.7749, srid=4326)

    point = geo_models.PointField(default=location, help_text="Represented as (longitude, latitude)")

    created_timestamp = CreationDateTimeField()
    modified_timestamp = ModificationDateTimeField()

    def __str__(self):
        return "%s - %s" % (self.label, self.point)


