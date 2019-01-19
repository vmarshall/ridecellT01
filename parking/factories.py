from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from factory.fuzzy import BaseFuzzyAttribute
from faker import Factory as FakerFactory
import random
# import factory
# from factory import DjangoModelFactory
from factory import DjangoModelFactory, LazyAttribute
from factory import Factory
from parking.models import ParkingSpot

faker = FakerFactory().create()

location = Point(-122.4194, 37.7749, srid=4326)


class SamplePoint(BaseFuzzyAttribute):
    def fuzz(self):
        return Point(random.uniform(-122.0, -123.0),
                     random.uniform(37.0, 38.0), srid=4326)

class UserFactory(DjangoModelFactory):
    class Meta:
        model = 'auth.User'
        django_get_or_create = (
            'username',
            'email'
        )

    username = LazyAttribute(lambda x: faker.name())
    email = LazyAttribute(lambda x: faker.email())

class ParkingSpotFactory(DjangoModelFactory):

    class Meta:
        model = ParkingSpot
        django_get_or_create = (
            'label',
            'point'
        )

    label = LazyAttribute(lambda x: faker.address())
    point = SamplePoint().fuzz()