"""Test suit for model customer"""

from datetime import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from point_of_sale.api.models import Customer
from point_of_sale.api.tests import create_customer_data


class CustomerTest(TestCase):
    def setUp(self):
        self.obj = Customer(
            **create_customer_data()
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Customer.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual(create_customer_data()['name'], str(self.obj))

    def test_correct_email(self):
        self.assertEqual(create_customer_data()['email'], self.obj.email)
