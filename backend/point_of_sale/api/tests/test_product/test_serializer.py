from django.test import TestCase

from point_of_sale.api.tests import create_product_data
from point_of_sale.api.serializers import ProductSerializer


def make_validated_serializer(**kwargs):
    data = create_product_data()
    data = dict(data, **kwargs)
    serializer = ProductSerializer(data=data)
    serializer.is_valid()

    return serializer


class ProductTestSerializer(TestCase):
    def test_has_fields(self):
        expected = ['id', 'name', 'description', 'price',
                    'minimum_stock', 'stock']
        serializer = ProductSerializer()
        self.assertEqual(expected, list(serializer.fields))

    def test_is_valid(self):
        serializer = make_validated_serializer()
        self.assertFalse(serializer.errors)

    def test_incorrect_price(self):
        serializer = make_validated_serializer(price='762,90')
        self.assertIn('price', serializer.errors)

    def test_incorrect_stock(self):
        serializer = make_validated_serializer(stock='xa')
        self.assertIn('stock', serializer.errors)

    def test_incorrect_minimum_stock(self):
        serializer = make_validated_serializer(minimum_stock='xa')
        self.assertIn('minimum_stock', serializer.errors)

    def test_incorrect_description(self):
        serializer = make_validated_serializer(description='')
        self.assertIn('description', serializer.errors)
