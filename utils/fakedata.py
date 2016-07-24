from vehicles.models import VehicleManufacturer


_manufacturer = 0


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