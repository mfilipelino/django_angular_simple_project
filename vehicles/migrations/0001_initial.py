# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=64)),
                ('mileage', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleManufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('motor', models.IntegerField(default=1000)),
                ('vehicle_type', models.CharField(max_length=3, choices=[(b'CAR', b'car'), (b'MOT', b'mot')])),
                ('manufacturer', models.ForeignKey(to='vehicles.VehicleManufacturer')),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_model',
            field=models.ForeignKey(to='vehicles.VehicleModel'),
        ),
    ]
