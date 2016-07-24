import json
from django.test.client import Client
from django.test.testcases import TestCase
from utils import fakedata
from django.core.urlresolvers import reverse

class ManufacturerApiTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        super(ManufacturerApiTest, cls).setUpTestData()
        for i in range(10):
            fakedata.create_manufacturer()

    def test_get_id(self):

        c = Client()
        response = c.get(reverse('api_manufactures', kwargs={'manufacture_id': 1}))
        self.assertEqual(response.status_code , 200)
        self.assertEqual(response.data['id'], 1)

    def test_get_filters(self):

        c = Client()
        response = c.get(reverse('api_list_manufactures'))
        self.assertEqual(response.status_code , 200)
        self.assertEqual(len(response.data['manufacturers']), 10)

        # filters = {'name' : 'manufac0v'}
        # data = {
        #      'filters' : json.dumps(filters)
        # }
        # response = c.get(reverse('api_list_manufactures'))
        # self.assertEqual(response.status_code , 200)
        # self.assertEqual(len(response.data['manufacturers']), 1)
