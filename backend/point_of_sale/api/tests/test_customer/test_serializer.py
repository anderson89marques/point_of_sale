"""Test suit for customer serializers"""

from django.test import TestCase

from point_of_sale.api.serializers import CustomerSerializer
from point_of_sale.api.tests import create_customer_data


def make_validated_serializer(**kwargs):
    data = create_customer_data()
    data = dict(data, **kwargs)
    serializer = CustomerSerializer(data=data)
    serializer.is_valid()

    return serializer


class CustomerSerializerTest(TestCase):
    def test_has_fields(self):
        expected = ['id', 'name', 'age', 'email', 'phone']
        serializer = CustomerSerializer()
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
