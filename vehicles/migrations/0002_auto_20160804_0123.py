# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='color',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vehiclemodel',
            name='vehicle_type',
            field=models.CharField(max_length=3, choices=[('CAR', 'car'), ('BIKE', 'bike')]),
        ),
    ]
