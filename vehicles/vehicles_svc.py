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


def get_manufacturer(manufacture_id, as_dict=False):

    filters = {
        'id' : manufacture_id
    }
    result = list_manufacturer(filters, as_dict=as_dict)

    if result['manufacturers'] :
        return result['manufacturers'][0]
    else:
        return None

def list_manufacturer(filters=None, as_dict=False):

    if filters is None:
        filters = {}

    query = VehicleManufacturer.objects.all()


    if 'name' in filters:
        query = query.filter(name=filters['name'])
    if 'id' in filters:
        query = query.filter(id=filters['id'])
    if 'name_contains' in filters:
        query = query.filter(name__icontains=filters['name_contains'])

    manufacturers = [vehicle.to_dict() if as_dict else vehicle for vehicle in query]

    result = {
        'manufacturers' : manufacturers
    }

    return  result



