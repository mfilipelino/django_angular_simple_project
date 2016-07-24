from django.test import TestCase
from utils.fakedata import create_manufacturer
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
             fakedata.create_manufacturer()

    def test_save_vehicle_model_no_exist_object_return_none(self):

        vehicle_model_dict = {}
        vehicle_model_dict['id'] = -1
        vehicle_model = vehicles_svc.save_vehiclemodel(vehicle_model_dict)
        self.assertIsNone(vehicle_model)

    def test_vehicle_model_name_(self):

        v = VehicleModel()
        vehicle_model_dict = {'name': 'Corola', 'manufacturer' : create_manufacturer()}
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