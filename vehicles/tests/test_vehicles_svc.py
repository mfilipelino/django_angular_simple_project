from django.test import TestCase
from vehicles import vehicles_svc
from utils import fakedata


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
        self.assertEqual(len(result['manufactures']), 10)

    def test_list_manufacturer_filter_name(self):
        filter = {
            'name': 'manufac0v'
        }
        result = vehicles_svc.list_manufacturer(filter)
        self.assertEqual(len(result['manufactures']), 1)

    def test_list_manufacturer_filter_name_contains(self):
        filter = {
            'name_contains': 'manufac'
        }

        result = vehicles_svc.list_manufacturer(filter)
        self.assertEqual(len(result['manufactures']), 10)

    def test_list_manufacturer_filter_none(self):
        result = vehicles_svc.list_manufacturer()
        self.assertEqual(len(result['manufactures']), 10)

    def test_delete_manufacture_id_exist(self):
        manufactures_dict_list = vehicles_svc.list_manufacturer()
        manufactures = manufactures_dict_list['manufactures']
        manufacture = manufactures[0]
        result = vehicles_svc.delete_manufacturer(manufacture.id)
        self.assertEqual(result, True)

    def test_delete_manufacture_id_doesnt_exist(self):
        result = vehicles_svc.delete_manufacturer(-1)
        self.assertEqual(result, False)


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
        vehicle_model_dict = {'name': 'Corola', 'manufacturer': fakedata.create_manufacturer()}
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
        vehicle_model_dict = {'name': 'S10', 'manufacturer': fakedata.create_manufacturer()}
        vehicle_model = vehicles_svc.save_vehiclemodel(vehicle_model_dict)
        id = vehicle_model.id
        vehicle_model = vehicles_svc.get_vehicle_model(id)
        self.assertEqual(vehicle_model.id, id)

    def test_list_vehicle_model(self):
        result = vehicles_svc.list_vehicle_model()
        self.assertEqual(len(result['vehicles_models']), 10)

    def test_list_vehicle_model_filter(self):
        filter = {
            'name': 'model0',
            'manufacturer_id': 1,
            'motor': 1000
        }

        result = vehicles_svc.list_vehicle_model(filter)
        self.assertEqual(len(result['vehicles_models']), 1)

    def test_list_vehicle_model_filter_contains(self):
        filter = {
            'name_contains': 'model'
        }

        result = vehicles_svc.list_vehicle_model(filter)
        self.assertEqual(len(result['vehicles_models']), 10)

    def test_delete_vehicle_model_id_exist(self):
        vehicles_model_dict_list = vehicles_svc.list_vehicle_model()
        vehicles_model = vehicles_model_dict_list['vehicles_models']
        vehicle_model = vehicles_model[0]
        result = vehicles_svc.delete_vehicle_model(vehicle_model.id)
        self.assertEqual(result, True)

    def test_delete_vehicle_model_id_doesnt_exist(self):
        result = vehicles_svc.delete_vehicle_model(-1)
        self.assertEqual(result, False)


class VehicleTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        super(VehicleTest, cls).setUpTestData()
        cls.vehicle_mock_lst = []
        for i in range(10):
            cls.vehicle_mock_lst.append(fakedata.create_vehicle(year=2000, color='vermelho'))

    def test_get_vehicle_not_exist(self):
        vehicle = vehicles_svc.get_vehicle(-1)
        self.assertIsNone(vehicle)

    def test_get_vehicle(self):
        vehicle_mock = self.vehicle_mock_lst[0]
        vehicle = vehicles_svc.get_vehicle(vehicle_mock.id)
        self.assertEqual(vehicle.id, vehicle_mock.id)

    def test_save_vehicle_no_exist_object_return_none(self):
        vehicle_dict = {}
        vehicle_dict['id'] = -1
        vehicle = vehicles_svc.save_vehicle(vehicle_dict)
        self.assertIsNone(vehicle)

    def test_vehicle_year(self):
        vehicle_dict = {'year': self.vehicle_mock_lst[0].year,
                        'vehicle_model_id': self.vehicle_mock_lst[0].vehicle_model_id}
        vehicle = vehicles_svc.save_vehicle(vehicle_dict)
        self.assertEqual(vehicle.year, self.vehicle_mock_lst[0].year)

        vehicle_model_dict = vehicle.to_dict()
        del vehicle_model_dict['year']
        id = vehicle_model_dict['id']
        self.assertEqual(vehicle.id, id)
        self.assertEqual(vehicle.year, self.vehicle_mock_lst[0].year)

        vehicle_dict = vehicle.to_dict()
        vehicle_dict['year'] = 2000
        vehicle = vehicles_svc.save_vehicle(vehicle_dict)
        self.assertEqual(vehicle.year, 2000)

    def test_list_vehicle_no_filter(self):
        vehicle_dict = {}
        result = vehicles_svc.list_vehicles(vehicle_dict)
        self.assertEqual(len(result['vehicles']), 10)

    def test_list_vehicle_filter(self):
        filter = {
            'year': '2000',
            'color': 'vermelho',
            'mileage': 100000,
            'vehicle_model_id': 1
        }

        result = vehicles_svc.list_vehicles(filter)
        self.assertEqual(len(result['vehicles']), 1)

    def test_list_vehicle_filter_contains(self):
        filter = {
            'color_contains': 'ver'
        }

        result = vehicles_svc.list_vehicles(filter)
        self.assertEqual(len(result['vehicles']), 10)

    def test_list_vehicle_model_filter_none(self):
        result = vehicles_svc.list_vehicles()
        self.assertEqual(len(result['vehicles']), 10)

    def test_delete_vehicle_id_exist(self):
        vehicles_dict_list = vehicles_svc.list_vehicles()
        vehicles = vehicles_dict_list['vehicles']
        vehicle = vehicles[0]
        result = vehicles_svc.delete_vehicle(vehicle.id)
        self.assertEqual(result, True)

    def test_delete_vehicles_id_doesnt_exist(self):
        result = vehicles_svc.delete_vehicle(-1)
        self.assertEqual(result, False)
