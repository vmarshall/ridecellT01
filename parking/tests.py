from django.test import TestCase

from django.test import TestCase
import factory.django, random
from django.contrib.auth.models import User
from factory import RelatedFactory
from factory.fuzzy import BaseFuzzyAttribute
from parking.models import ParkingSpot
from django.contrib.gis.geos import Point

from parking.models import Car

class SamplePoint(BaseFuzzyAttribute):
    def fuzz(self):
        return Point(random.uniform(-180.0, 180.0),
                     random.uniform(-90.0, 90.0))

class UserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = 'Fred'
    last_name = 'Flinstone'
    admin = False

class ParkingSpotFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ParkingSpot
        django_get_or_create = (
            'label',
            'location'
        )
    label = 'Ridecell Corporate'
    location = SamplePoint()


# class CarFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Car
#         django_get_or_create = (
#
#             'location',
#             'search_radius'
#         )
#     # driver = 'User Car'
#     driver = RelatedFactory(UserFactory, 'user', action=User.ACTION_CREATE)
#     location = SamplePoint()
#     search_radius = 5



class ParkingSpotTest(TestCase):
    def test_create_parking_spot(self):

        spot = ParkingSpotFactory()

        parking_spots = ParkingSpot.objects.all()
        self.assertEqual(len(parking_spots), 1)
        test_spot = parking_spots[0]
        self.assertEqual(test_spot, spot)

        self.assertEqual(test_spot.label, 'Ridecell Corporate')


# class CarTest(TestCase):
#     def test_create_car(self):
#         car = CarFactory()
#         spot = ParkingSpotFactory(car=car)
#         all_spots = ParkingSpot.objects.all()
#         self.assertEqual(len(all_spots), 1)
#         first_spot = all_spots[0]
#         self.assertEqual(first_spot, spot)
#         self.assertEqual(first_spot.label, 'Ridecell Corporate')

