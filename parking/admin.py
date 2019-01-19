

# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import ParkingSpot


@admin.register(ParkingSpot)
class ParkingSpotAdmin(OSMGeoAdmin):
    list_display = (
        'id',
        'rcpid',
        'owner',
        'reserved',
        'label',
        'point',
        'created_timestamp',
        'modified_timestamp',
    )
    list_filter = (
        'owner',
        'reserved',
        'created_timestamp',
        'modified_timestamp',
    )
