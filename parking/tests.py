from django.test import TestCase

from django.test import TestCase
import factory.django, random
from django.contrib.auth.models import User
from factory import RelatedFactory
from factory.fuzzy import BaseFuzzyAttribute

from parking.factories import ParkingSpotFactory
from parking.models import ParkingSpot










class ParkingSpotTest(TestCase):
    def test_create_parking_spot(self):

        spot = ParkingSpotFactory()

        # parking_spots = ParkingSpot.objects.all()
        # self.assertEqual(len(parking_spots), 1)
        # test_spot = parking_spots[0]
        # self.assertEqual(test_spot, spot)
        #
        # self.assertEqual(test_spot.label, 'Ridecell Corporate')

