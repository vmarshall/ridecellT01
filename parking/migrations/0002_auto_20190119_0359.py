# Generated by Django 2.1.5 on 2019-01-19 03:59

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkingspot',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(38.907636, 122.419), help_text='Represented as (longitude, latitude)', srid=4326),
        ),
        migrations.AddField(
            model_name='parkingspot',
            name='test',
            field=models.CharField(default='test', max_length=128),
        ),
    ]
