from vehicles.models import VehicleManufacturer, VehicleModel, Vehicle
import random

_manufacturer = 0
_vehicle_model = 0
_vehicle = 0

def create_manufacturer():

    global _manufacturer
    name = 'manufac' + str(_manufacturer) + 'v'
    manufacturer_dict = {
        'name' : name
    }
    _manufacturer += 1
    manufacturer = VehicleManufacturer(**manufacturer_dict)
    manufacturer.save()
    return  manufacturer


def create_vehicle_model():

    global _vehicle_model
    name = 'model' + str(_vehicle_model)
    dic = {
        'name' : name,
        'manufacturer' : create_manufacturer(),
        'motor' : 1000,
        'vehicle_type' : VehicleModel.TYPE_CAR
    }

    _vehicle_model += 1
    vehicleModel = VehicleModel(**dic)
    vehicleModel.save()
    return  vehicleModel

def create_vehicle(**kwargs):

    global _vehicle
    name = 'vehicle' + str(_vehicle)
    years = [1999, 2010, 2015]
    colors = ['azul', 'prata', 'preto']


    _vehicle += 1

    dic = {
        'vehicle_model' : create_vehicle_model(),
        'year' : kwargs.get('year', random.choice(years)),
        'color' : kwargs.get('color', random.choice(colors)),
        'mileage' : kwargs.get('mileage', 100000)
    }

    vehicle = Vehicle(**dic)
    vehicle.save()
    return  vehicle