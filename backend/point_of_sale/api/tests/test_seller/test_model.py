"""Test suit for model seller"""

from datetime import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from point_of_sale.api.models import Seller
from point_of_sale.api.tests import create_seller_data


class SellerTest(TestCase):
    def setUp(self):
        self.obj = Seller(
            **create_seller_data()
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Seller.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual(create_seller_data()['name'], str(self.obj))

    def test_correct_email(self):
        self.assertEqual(create_seller_data()['email'], self.obj.email)

