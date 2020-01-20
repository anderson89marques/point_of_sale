"""Test suit for model product"""

from datetime import datetime

from django.test import TestCase

from point_of_sale.api.models import Product
from point_of_sale.api.tests import create_product_data


class ProductTest(TestCase):
    def setUp(self):
        self.obj = Product.objects.create(**create_product_data())

    def test_create(self):
        self.assertTrue(Product.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual("Telefone", str(self.obj))

