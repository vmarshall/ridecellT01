# Generated by Django 2.1.5 on 2019-01-19 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0007_auto_20190119_0610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parkingspot',
            old_name='available',
            new_name='reserved',
        ),
    ]