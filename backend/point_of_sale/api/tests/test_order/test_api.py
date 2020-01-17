import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from point_of_sale.api.models import Customer, Order, Product, Seller
from point_of_sale.api.tests import (create_customer_data, create_product_data,
                                     create_seller_data)


class BaseTest(APITestCase):
    def setUp(self):
        seller = Seller.objects.create(**create_seller_data())
        customer = Customer.objects.create(**create_customer_data())
        product = Product.objects.create(**create_product_data())
        self.data = {
            "customer_id": customer.pk,
            "seller_id": seller.pk,
            "total_price": 200.90,
            "itens": [{"id": product.pk, "quantity": 1, "price": 200.90}]
        }


class OrderCreateValidPostTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.url = reverse('order-list')
        self.response = self.client.post(self.url, self.data, format='json')

    def test_create_order_status_code(self):
        """Response must have status_code 201 CREATED"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_create_order(self):
        """There must be one order"""
        self.assertEqual(Order.objects.count(), 1)

    def test_order_total_commission(self):
        order = Order.objects.first()
        self.assertEqual(Order.objects.count(), 1)
    
    def test_create_order_status_code_without_seller_id(self):
        data = self.data.copy()
        data['seller_id'] = None
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class OrderCreateInvalidTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.url = reverse('order-list')
    
    def test_create_order_invalid_post_status_code(self):
        data = self.data.copy()
        data['customer_id'] = None
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_order_invalid_post_without_custmer_id(self):
        data = self.data.copy()
        del data['customer_id']
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(json.loads(response.content), {
                         'customer_id': ['This field is required.']})

    def test_not_create_order(self):
        self.assertEqual(Order.objects.count(), 0)
