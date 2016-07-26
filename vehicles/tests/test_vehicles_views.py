import json
from django.test.client import Client
from django.test.testcases import TestCase
from utils import fakedata
from django.core.urlresolvers import reverse


class ManufacturerApiTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        super(ManufacturerApiTest, cls).setUpTestData()
        cls.manufacturer_mock_lst = []
        for i in range(10):
            cls.manufacturer_mock_lst.append(fakedata.create_manufacturer())

    def test_get_id(self):
        c = Client()
        response = c.get(reverse('api_manufactures', kwargs={'manufacture_id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 1)

    def test_get_filters(self):
        manufacture = self.manufacturer_mock_lst[0]
        filters = {'name': manufacture.name}
        data = {
            'filters': json.dumps(filters)
        }
        c = Client()
        response = c.get(reverse('api_list_manufactures'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['manufacturers']), 1)


class VehicleModelApiTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        super(VehicleModelApiTest, cls).setUpTestData()
        cls.vehicle_models_mock_lst = []
        for i in range(10):
            cls.vehicle_models_mock_lst.append(fakedata.create_vehicle_model())

    def test_get_id(self):
        c = Client()
        response = c.get(reverse('api_vehicles_model', kwargs={'vehicles_model_id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 1)

    def test_get_filters(self):
        vehicle_model = self.vehicle_models_mock_lst[0]
        filters = {'name': vehicle_model.name}
        data = {
            'filters': json.dumps(filters)
        }
        c = Client()
        response = c.get(reverse('api_list_vehicles_models'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['vehicles_models']), 1)


class VehicleApiTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        super(VehicleApiTest, cls).setUpTestData()
        for i in range(10):
            fakedata.create_vehicle()

    def test_get_id(self):
        c = Client()
        response = c.get(reverse('api_vehicles', kwargs={'vehicles_id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 1)
