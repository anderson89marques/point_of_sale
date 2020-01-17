from django.urls import reverse

from rest_framework import status

from point_of_sale.api.tests.test_order import BaseTest
from point_of_sale.api.models import OrderItem


class OrderItemTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.url = reverse('order-list')
        self.response = self.client.post(self.url, self.data, format='json')
    
    def test_create_order_status_code(self):
        """Response must have status_code 201 CREATED"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_create_order_item(self):
        """There must be one OrderItem"""
        self.assertEqual(OrderItem.objects.count(), 1)
    
    def test_create_order_item_commission(self):
        """Has commission calculated"""
        commission = OrderItem.objects.first().commission
        self.assertTrue(commission)