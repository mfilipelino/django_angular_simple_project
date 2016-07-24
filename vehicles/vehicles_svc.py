from logging import exception
from vehicles.models import VehicleManufacturer
from vehicles.models import *



def save_manufacturer(manufacturer_dict):

    try:
        if 'id' in manufacturer_dict:
            manufacturer = VehicleManufacturer.objects.get(id=manufacturer_dict['id'])
            manufacturer.name = manufacturer_dict.get('name', manufacturer.name)
        else:
            manufacturer = VehicleManufacturer(**manufacturer_dict)

        manufacturer.save()
        return manufacturer

    except VehicleManufacturer.DoesNotExist:
        return None


def get_manufacturer(manufacturer_id):

    filters = {
        'id' : manufacturer_id
    }
    result = list_manufacturer(filters)

    if result['manufacturers'] :
        return result['manufacturers'][0]
    else:
        return None

def list_manufacturer(filters=None):

    if filters is None:
        filters = {}

    query = VehicleManufacturer.objects.all()


    if 'name' in filters:
        query = query.filter(name=filters['name'])
    if 'id' in filters:
        query = query.filter(id=filters['id'])
    if 'name_contains' in filters:
        query = query.filter(name__icontains=filters['name_contains'])

    manufacturers = list(query)
    result = {
        'manufacturers' : manufacturers
    }

    return  result



