"""Test suit for product API"""
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from point_of_sale.api.models import Product
from point_of_sale.api.tests import create_product_data


class ProductValidPostTest(APITestCase):
    def setUp(self):
        self.url = reverse('product-list')
        self.data = create_product_data()
        self.response = self.client.post(self.url, self.data)

    def test_create_product_status_code(self):
        """Response must have status_code 201 CREATED"""

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_create_product(self):
        """There must be one product"""
        self.assertEqual(Product.objects.count(), 1)


class ProductInvalidPostTest(APITestCase):
    def setUp(self):
        self.url = reverse('product-list')

    def test_create_product(self):
        """There must be one product"""

        self.assertEqual(Product.objects.count(), 0)
    
    def test_create_product_invalid_post_incorrect_price(self):
        data = create_product_data(price='762,90')
        response = self.client.post(self.url, data)
        self.assertEqual(json.loads(response.content), {
                         'price': ['A valid number is required.']})
    
    def test_create_product_invalid_post_string_price(self):
        data = create_product_data(price='sds')
        response = self.client.post(self.url, data)
        self.assertEqual(json.loads(response.content), {
                         'price': ['A valid number is required.']})

    def test_incorrect_minimum_description(self):
        data = create_product_data(minimum_stock='xa')
        response = self.client.post(self.url, data)
        self.assertEqual(json.loads(response.content), {
                         'minimum_stock': ['A valid integer is required.']})

    def test_incorrect_stock(self):
        data = create_product_data(stock='xa')
        response = self.client.post(self.url, data)
        self.assertEqual(json.loads(response.content), {
                         'stock': ['A valid integer is required.']})

    def test_incorrect_minimum_stock(self):
        data = create_product_data(minimum_stock='xa')
        response = self.client.post(self.url, data)
        self.assertEqual(json.loads(response.content), {
                         'minimum_stock': ['A valid integer is required.']})