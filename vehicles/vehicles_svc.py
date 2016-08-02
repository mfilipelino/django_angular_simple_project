from vehicles.models import VehicleManufacturer, VehicleModel, Vehicle


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
        'id': manufacture_id
    }
    result = list_manufacturer(filters, as_dict=as_dict)

    if result['manufactures']:
        return result['manufactures'][0]
    else:
        return None


def delete_manufacturer(manufacture_id):
    filters = {
        'id': manufacture_id
    }
    result = list_manufacturer(filters)

    if result['manufactures']:
        result['manufactures'][0].delete()
        return True
    else:
        return False


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
        'manufactures': manufacturers
    }

    return result


def save_vehiclemodel(vehicle_model_dict):
    try:
        if 'id' in vehicle_model_dict:
            vehicle_model = VehicleModel.objects.get(id=vehicle_model_dict['id'])
            vehicle_model.name = vehicle_model_dict.get('name', vehicle_model.name)
            vehicle_model.manufacturer_id = vehicle_model_dict.get('manufacturer_id', vehicle_model.manufacturer_id)
            vehicle_model.motor = vehicle_model_dict.get('motor', vehicle_model.motor)
            vehicle_model.vehicle_type = vehicle_model_dict.get('vehicle_type', vehicle_model.vehicle_type)
        else:
            vehicle_model = VehicleModel(**vehicle_model_dict)

        vehicle_model.save()
        return vehicle_model

    except VehicleModel.DoesNotExist:
        return None


def delete_vehicle_model(vehicles_model_id):
    filters = {
        'id': vehicles_model_id
    }
    result = list_vehicle_model(filters)

    if result['vehicles_models']:
        result['vehicles_models'][0].delete()
        return True
    else:
        return False


def get_vehicle_model(vehicle_model_id, as_dict=False):
    filter = {
        'id': vehicle_model_id
    }

    result = list_vehicle_model(filter, as_dict=as_dict)
    if result['vehicles_models']:
        return result['vehicles_models'][0]
    else:
        return None


def list_vehicle_model(filters=None, as_dict=False):
    filters = filters or {}

    query = VehicleModel.objects.all()
    if 'name' in filters:
        query = query.filter(name=filters['name'])
    if 'motor' in filters:
        query = query.filter(motor=filters['motor'])
    if 'manufacturer_id' in filters:
        query = query.filter(manufacturer_id=filters['manufacturer_id'])
    if 'id' in filters:
        query = query.filter(id=filters['id'])
    if 'name_contains' in filters:
        query = query.filter(name__icontains=filters['name_contains'])

    vehicles_models = [vehicles_model.to_dict() if as_dict else vehicles_model for vehicles_model in query]

    result = {
        'vehicles_models': vehicles_models
    }

    return result


def save_vehicle(vehicle_dict):
    try:
        if 'id' in vehicle_dict:
            vehicle = Vehicle.objects.get(id=vehicle_dict['id'])
            vehicle.vehicle_model_id = vehicle_dict.get('vehicle_model_id', vehicle.vehicle_model_id)
            vehicle.color = vehicle_dict.get('color', vehicle.color)
            vehicle.mileage = vehicle_dict.get('mileage', vehicle.mileage)
            vehicle.year = vehicle_dict.get('year', vehicle.year)
        else:
            vehicle = Vehicle(**vehicle_dict)

        vehicle.save()
        return vehicle

    except Vehicle.DoesNotExist:
        return None


def get_vehicle(vehicle_id, as_dict=False):
    filter = {
        'id': vehicle_id
    }

    result = list_vehicles(filter, as_dict=as_dict)
    if result['vehicles']:
        return result['vehicles'][0]
    else:
        return None


def list_vehicles(filters=None, as_dict=False):
    filters = filters or {}

    query = Vehicle.objects.all()
    if 'year' in filters:
        query = query.filter(year=filters['year'])
    if 'color' in filters:
        query = query.filter(color=filters['color'])
    if 'mileage' in filters:
        query = query.filter(mileage=filters['mileage'])
    if 'id' in filters:
        query = query.filter(id=filters['id'])
    if 'vehicle_model_id' in filters:
        query = query.filter(vehicle_model_id=filters['vehicle_model_id'])
    if 'color_contains' in filters:
        query = query.filter(color__icontains=filters['color_contains'])

    vehicles = [vehicle.to_dict() if as_dict else vehicle for vehicle in query]

    result = {
        'vehicles': vehicles
    }
    return result
