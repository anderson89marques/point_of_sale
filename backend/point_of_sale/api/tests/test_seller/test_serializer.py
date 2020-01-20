"""Test suit for seller serializers"""

from django.test import TestCase

from point_of_sale.api.tests import create_seller_data
from point_of_sale.api.serializers import SellerSerializer


def make_validated_serializer(**kwargs):
    data = create_seller_data()
    data = dict(data, **kwargs)
    serializer = SellerSerializer(data=data)
    serializer.is_valid()

    return serializer


class SellerSerializerTest(TestCase):
    def test_has_fields(self):
        expected = ['id', 'name', 'age', 'email', 'phone', 'identify']
        serializer = SellerSerializer()
        self.assertEqual(expected, list(serializer.fields))
    
    def test_is_valid(self):
        serializer = make_validated_serializer()
        self.assertFalse(serializer.errors)

    def test_incorrect_email(self):
        serializer = make_validated_serializer(email='andersonoanjo18@')
        self.assertIn('email', serializer.errors)

    def test_incorrect_name(self):
        serializer = make_validated_serializer(name='Anderson Marques89')
        self.assertIn('name', serializer.errors)

    def test_incorrect_phone_number(self):
        serializer = make_validated_serializer(phone='99274-5052')
        self.assertIn('phone', serializer.errors)
    
    def test_incorrect_age(self):
        serializer = make_validated_serializer(age='@')
        self.assertIn('age', serializer.errors)