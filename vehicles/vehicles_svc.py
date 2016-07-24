from vehicles.models import VehicleManufacturer, VehicleModel


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

    manufacturers = [manufacturer.to_dict() if as_dict else manufacturer for manufacturer in query]

    result = {
        'manufacturers' : manufacturers
    }

    return  result


def save_vehiclemodel(vehicle_model_dict):
    
    try:
        if 'id' in vehicle_model_dict:
            vehicle_model = VehicleModel.objects.get(id=vehicle_model_dict['id'])
            vehicle_model.name = vehicle_model_dict.get('name', vehicle_model.name)
            vehicle_model.manufacturer_id= vehicle_model_dict.get('manufacturer_id', vehicle_model.manufacturer_id)
            vehicle_model.motor = vehicle_model_dict.get('motor', vehicle_model.motor)
            vehicle_model.vehicle_type = vehicle_model_dict.get('type_vehicle', vehicle_model.vehicle_type)
        else:
            vehicle_model = VehicleModel(**vehicle_model_dict)

        vehicle_model.save()
        return  vehicle_model

    except VehicleModel.DoesNotExist:
        return None




