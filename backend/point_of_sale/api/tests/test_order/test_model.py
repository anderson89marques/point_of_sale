
"""Test suit for model order"""

from datetime import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from point_of_sale.api.models import Customer, Order, Seller
from point_of_sale.api.tests import create_customer_data, create_seller_data 


class OrderTest(TestCase):
    def setUp(self):
        seller = Seller.objects.create(**create_seller_data())
        customer = Customer.objects.create(**create_customer_data())
        self.order = Order.objects.create(seller=seller, customer=customer, total_price=100)
    
    def test_create(self):
        self.assertTrue(Customer.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.order.created_at, datetime)