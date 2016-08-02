from django.db import models


class VehicleManufacturer(models.Model):

    name = models.CharField(max_length=50, blank=False, null=False, unique=True)

    def to_dict(self):
        vehicle_manufacturer_dict = {
            'id': self.id,
            'name': self.name
        }
        return vehicle_manufacturer_dict


class VehicleModel(models.Model):

    TYPE_CAR = 'CAR'
    TYPE_MOT = 'BIKE'
    TYPE_CHOICES = (
        (TYPE_CAR, 'car'),
        (TYPE_MOT, 'bike'),
    )

    vehicle_type = models.CharField(max_length=3, blank=False, null=False, choices=TYPE_CHOICES)
    name = models.CharField(max_length=50, blank=False, null=False)
    manufacturer = models.ForeignKey('VehicleManufacturer')
    motor = models.IntegerField(blank=False, null=False, default=1000)

    def to_dict(self):
        vechicle_model_dict = {
            'id': self.id,
            'name': self.name,
            'manufacturer_id': self.manufacturer_id,
            'motor': self.motor,
            'vehicle_type': self.vehicle_type
        }
        return vechicle_model_dict


class Vehicle(models.Model):

    year = models.PositiveIntegerField(blank=False, null=False)
    color = models.CharField(max_length=50, blank=False, null=False)
    vehicle_model = models.ForeignKey('vehicles.VehicleModel')
    mileage = models.PositiveIntegerField(blank=False, null=False, default=0)

    def to_dict(self):
        dic = {
            'id': self.id,
            'vehicle_model_id': self.vehicle_model_id,
            'year': self.year,
            'mileage': self.mileage,
            'color': self.color
        }
        return dic
