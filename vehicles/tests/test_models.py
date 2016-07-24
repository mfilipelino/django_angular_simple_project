from django.test import TestCase
from vehicles import vehicles_svc

class ManufacturerTest(TestCase):

    def setUp(self):
        pass

    def test_save_manufacturer_isnone(self):

        manufacturer_dict = {}
        manufacturer_dict['id'] = 1
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


    def test_get_manufacturer(self):

        manufacturer_dict = {'name': 'Toyota'}
        manufacturer = vehicles_svc.save_manufacturer(manufacturer_dict)
        id = manufacturer.id
        manufacturer = vehicles_svc.get_manufacturer(id)
        self.assertEqual(manufacturer.id, id)

    def test_get_manufacturer_isnone(self):
        
