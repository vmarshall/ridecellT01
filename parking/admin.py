# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Car, ParkingSpot


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'driver', 'location')
    list_filter = ('driver',)


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'rcpid',
        'owner',
        'available',
        'label',
        'lon',
        'lat',
        'location',
        'created_timestamp',
        'modified_timestamp',
    )
    list_filter = (
        'owner',
        'available',
        'created_timestamp',
        'modified_timestamp',
    )
