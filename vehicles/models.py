from django.db import models


class VehicleManufacturer(models.Model):

    name = models.CharField(max_length=50, blank=False, null=False, unique=True)


    def to_dict(self):
        vehicle_manufacturer_dict = {
            'id' : self.id,
            'name' : self.name
        }
        return vehicle_manufacturer_dict


class VehicleModel(models.Model):

    TYPE_CAR = 'CAR'
    TYPE_MOT = 'MOT'
    TYPE_CHOICES = (
        (TYPE_CAR, 'car'),
        (TYPE_MOT, 'mot'),
    )

    vehicle_type = models.CharField(max_length=3, blank=False, null=False, choices=TYPE_CHOICES)
    name = models.CharField(max_length=50, blank=False, null=False)
    manufacturer = models.ForeignKey('VehicleManufacturer')
    motor = models.IntegerField(blank=False, null=False, default=1000)

    def to_dict(self):
        dic = {
            'id' : self.id,
            'name' : self.name,
            'manufacturer' : self.manufacturer,
            'motor' : self.motor,
            'vehicle_type' : self.vehicle_type
        }
        return dic


class Vehicle(models.Model):
	
	vehicle_model = models.ForeignKey('vehicles.VehicleModel')
	year = models.PositiveIntegerField(blank=False, null=False)
	color = models.CharField(max_length=64, blank=False, null=False)
	mileage = models.PositiveIntegerField(blank=False, null=False, default=0)


