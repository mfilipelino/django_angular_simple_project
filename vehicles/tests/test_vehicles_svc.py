from django.test import TestCase
from utils import fakedata
from vehicles import vehicles_svc
from utils import fakedata
from vehicles.models import VehicleModel


class ManufacturerTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        super(ManufacturerTest, cls).setUpTestData()
        for i in range(10):
            fakedata.create_manufacturer()

    def test_save_manufacturer_no_exist_object_return_none(self):

        manufacturer_dict = {}
        manufacturer_dict['id'] = -1
        manufacturer_dict['name'] = 'Toyota'

        manufacturer = vehicles_svc.save_manufacturer(manufacturer_dict)
        self.assertIsNone(manufacturer)

    def test_save_manufacturer_name(self):

        manufacturer_dict = {'name': 'Toyota'}
        manufacturer = vehicles_svc.save_manufacturer(manufacturer_dict)
        self.assertEqual(manufacturer.name, 'Toyota')

        manufacturer_dict = manufacturer.to_dict()
        del manufacturer_dict['name']
        id = manufacturer_dict['id']
        manufacturer = vehicles_svc.save_manufacturer(manufacturer_dict)
        self.assertEqual(manufacturer.id, id)
        self.assertEqual(manufacturer.name, 'Toyota')

        manufacturer_dict = manufacturer.to_dict()
        manufacturer_dict['name'] = 'Honda'
        id = manufacturer_dict['id']
        manufacturer = vehicles_svc.save_manufacturer(manufacturer_dict)
        self.assertEqual(manufacturer.name, 'Honda')


    def test_get_manufacturer_not_exist(self):

        manufacturer = vehicles_svc.get_manufacturer(-1)
        self.assertIsNone(manufacturer)

    def test_get_manufacturer(self):

        manufacturer_dict = {'name': 'Toyota'}
        manufacturer = vehicles_svc.save_manufacturer(manufacturer_dict)
        id = manufacturer.id
        manufacturer = vehicles_svc.get_manufacturer(id)
        self.assertEqual(manufacturer.id, id)

    def test_list_manufacturer(self):

        manufacturer_dict = {}
        result = vehicles_svc.list_manufacturer(manufacturer_dict)
        self.assertEqual(len(result['manufacturers']), 10)

    def test_list_manufacturer_filter_name(self):

        filter = {
            'name' : 'manufac0v'
        }

        result = vehicles_svc.list_manufacturer(filter)
        self.assertEqual(len(result['manufacturers']), 1)


    def test_list_manufacturer_filter_name_contains(self):

        filter = {
            'name_contains' : 'manufac'
        }

        result = vehicles_svc.list_manufacturer(filter)
        self.assertEqual(len(result['manufacturers']), 10)

    def test_list_manufacturer_filter_none(self):

        result = vehicles_svc.list_manufacturer()
        self.assertEqual(len(result['manufacturers']), 10)

class VehicleModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
         super(VehicleModelTest, cls).setUpTestData()
         for i in range(10):
             fakedata.create_vehicle_model()

    def test_save_vehicle_model_no_exist_object_return_none(self):

        vehicle_model_dict = {}
        vehicle_model_dict['id'] = -1
        vehicle_model = vehicles_svc.save_vehiclemodel(vehicle_model_dict)
        self.assertIsNone(vehicle_model)

    def test_vehicle_model_name_(self):

        vehicle_model_dict = {'name': 'Corola', 'manufacturer' : fakedata.create_manufacturer()}
        vehicle_model = vehicles_svc.save_vehiclemodel(vehicle_model_dict)
        self.assertEqual(vehicle_model.name, 'Corola')

        vehicle_model_dict = vehicle_model.to_dict()
        del vehicle_model_dict['name']
        id = vehicle_model_dict['id']
        manufacturer = vehicles_svc.save_vehiclemodel(vehicle_model_dict)
        self.assertEqual(manufacturer.id, id)
        self.assertEqual(manufacturer.name, 'Corola')

        vehicle_model_dict = vehicle_model.to_dict()
        vehicle_model_dict['name'] = 'ranger'
        vehicle_model = vehicles_svc.save_vehiclemodel(vehicle_model_dict)
        self.assertEqual(vehicle_model.name, 'ranger')

    def test_get_vehicle_model_not_exist(self):

        vehicle_model = vehicles_svc.get_vehicle_model(-1)
        self.assertIsNone(vehicle_model)

    def test_get_vehicle_model(self):

        vehicle_model_dict = {'name': 'S10', 'manufacturer' : fakedata.create_manufacturer()}
        vehicle_model = vehicles_svc.save_vehiclemodel(vehicle_model_dict)
        id = vehicle_model.id
        vehicle_model = vehicles_svc.get_vehicle_model(id)
        self.assertEqual(vehicle_model.id, id)

    def test_list_vehicle_model(self):

        vehicle_model_dict = {}
        result = vehicles_svc.list_vehicle_model(vehicle_model_dict)
        self.assertEqual(len(result['vehicles_models']), 10)

    def test_list_vehicle_filter_name(self):

        filter = {
            'name' : 'model0'
        }

        result = vehicles_svc.list_vehicle_model(filter)
        self.assertEqual(len(result['vehicles_models']), 1)

    def test_list_vehicle_model_filter_name_contains(self):

        filter = {
            'name_contains' : 'model'
        }

        result = vehicles_svc.list_vehicle_model(filter)
        self.assertEqual(len(result['vehicles_models']), 10)

    def test_list_vehicle_model_filter_none(self):

        result = vehicles_svc.list_vehicle_model()
        self.assertEqual(len(result['vehicles_models']), 10)


class VehicleTest(TestCase):

    @classmethod
    def setUpTestData(cls):
         super(VehicleTest, cls).setUpTestData()
         for i in range(10):
             fakedata.create_vehicle(year=2000, color='vermelho')

    def test_save_vehicle_no_exist_object_return_none(self):

        vehicle_dict = {}
        vehicle_dict['id'] = -1
        vehicle = vehicles_svc.save_vehicle(vehicle_dict)
        self.assertIsNone(vehicle)

    def test_vehicle_year(self):

        vehicle_dict = {'year': 1988, 'vehicle_model' : fakedata.create_vehicle_model()}
        vehicle = vehicles_svc.save_vehicle(vehicle_dict)
        self.assertEqual(vehicle.year, 1988)

        vehicle_model_dict = vehicle.to_dict()
        del vehicle_model_dict['year']
        id = vehicle_model_dict['id']
        manufacturer = vehicles_svc.save_vehicle(vehicle_dict)
        self.assertEqual(vehicle.id, id)
        self.assertEqual(vehicle.year, 1988)

        vehicle_dict = vehicle.to_dict()
        vehicle_dict['year'] = 2000
        vehicle = vehicles_svc.save_vehicle(vehicle_dict)
        self.assertEqual(vehicle.year, 2000)

    def test_list_vehicle(self):

        vehicle_dict = {}
        result = vehicles_svc.list_vehicles(vehicle_dict)
        self.assertEqual(len(result['vehicles']), 10)

    def test_list_vehicle_filter_year(self):

        filter = {
            'year' : '2000'
        }

        result = vehicles_svc.list_vehicles(filter)
        self.assertEqual(len(result['vehicles']), 10)

    def test_list_vehicle_filter_color(self):

        filter = {
            'color' : 'vermelho'
        }

        result = vehicles_svc.list_vehicles(filter)
        self.assertEqual(len(result['vehicles']), 10)

    def test_list_vehicle_filter_color(self):

        filter = {
            'color' : 'vermelho'
        }

        result = vehicles_svc.list_vehicles(filter)
        self.assertEqual(len(result['vehicles']), 10)


    def test_list_vehicle_filter_mileage(self):

        filter = {
            'mileage' : 100000
        }

        result = vehicles_svc.list_vehicles(filter)
        self.assertEqual(len(result['vehicles']), 10)

    def test_list_vehicle_filter_color_contains(self):

        filter = {
            'color_contains' : 'ver'
        }

        result = vehicles_svc.list_vehicles(filter)
        self.assertEqual(len(result['vehicles']), 10)

    def test_list_vehicle_model_filter_none(self):

        result = vehicles_svc.list_vehicles()
        self.assertEqual(len(result['vehicles']), 10)