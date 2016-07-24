from vehicles.models import VehicleManufacturer, VehicleModel


_manufacturer = 0
_vehicle_model = 0

def create_manufacturer():

    name = 'manufac' + str(_manufacturer) + 'v'
    manufacturer_dict = {
        'name' : name
    }
    global _manufacturer
    _manufacturer += 1
    manufacturer = VehicleManufacturer(**manufacturer_dict)
    manufacturer.save()
    return  manufacturer


def create_vehicle_model():

    name = 'model' + str(_vehicle_model)
    dic = {
        'name' : name,
        'manufacturer' : create_manufacturer(),
        'motor' : 1000,
        'vehicle_type' : VehicleModel.TYPE_CAR
    }
    global _vehicle_model
    _vehicle_model += 1
    vehicleModel = VehicleModel(**dic)
    vehicleModel.save()
    return  vehicleModel