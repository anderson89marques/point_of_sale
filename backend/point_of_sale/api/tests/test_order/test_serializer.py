from django.test import TestCase

from point_of_sale.api.models import Customer, Seller, Order
from point_of_sale.api.serializers import (OrderCreateSerializer,
                                           OrderSerializer)
from point_of_sale.api.tests import create_customer_data, create_seller_data


def make_validated_serializer(**kwargs):
    seller = create_seller_data()
    customer = create_customer_data()
    itens = [{'id': 1, 'quantity': 1, 'price': 200.90}]
    data = {'total_price': 200.90, 'customer': customer,
            'seller': seller, 'itens': itens}
    data = dict(data, **kwargs)
    serializer = OrderSerializer(data=data)
    serializer.is_valid()

    return serializer


class OrderSerializerTest(TestCase):
    def test_has_fields(self):
        expected = ['id', 'total_price', 'itens', 'customer', 'seller']
        serializer = OrderSerializer()
        self.assertEqual(expected, list(serializer.fields))

    def test_is_valid(self):
        serializer = make_validated_serializer()
        self.assertFalse(serializer.errors)

    def test_empty_total_price(self):
        serializer = make_validated_serializer(total_price='')
        self.assertIn('total_price', serializer.errors)


class OrderCreateSerializerTest(TestCase):
    def setUp(self):
        self.seller = Seller.objects.create(**create_seller_data())
        self.customer = Customer.objects.create(**create_customer_data())

    def test_has_fields(self):
        expected = ['customer_id', 'customer',
                    'seller_id', 'seller', 'total_price', 'itens']
        serializer = OrderCreateSerializer()
        self.assertEqual(expected, list(serializer.fields))

    def test_is_valid(self):
        data = {
            'total_price': 200.90,
            'customer_id': self.customer.pk,
            'seller_id': self.seller.pk,
            'itens': [{'id': 1, 'quantity': 1, 'price': 200.90}]
        }
        serializer = OrderCreateSerializer(data=data)
        serializer.is_valid()
        self.assertFalse(serializer.errors)

