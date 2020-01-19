"""Test suit for customer API"""

import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from point_of_sale.api.models import Customer
from point_of_sale.api.tests import create_customer_data


class CustomerValidPostTest(APITestCase):
    def setUp(self):
        self.url = reverse('customer-list')
        self.data = create_customer_data()
        self.response = self.client.post(self.url, self.data)

    def test_create_customer_status_code(self):
        """Response must have status_code 201 CREATED"""

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_create_customer(self):
        """There must be one customer"""
        self.assertEqual(Customer.objects.count(), 1)


class CustomerNewPostInvalidTest(APITestCase):
    def setUp(self):
        self.url = reverse('customer-list')

    def test_create_customer_invalid_post_status_code(self):
        data = create_customer_data(name='Anderson Marques1')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_create_customer(self):
        self.assertEqual(Customer.objects.count(), 0)

    def test_create_customer_invalid_post_incorrect_name(self):
        data = create_customer_data(name='Anderson Marques1')
        response = self.client.post(self.url, data)
        self.assertEqual(
            json.loads(response.content), {'name': ['Name should not contains digit.']})

    def test_create_customer_invalid_post_incorrect_email(self):
        data = create_customer_data(email='andersonoanjo18')
        response = self.client.post(self.url, data)
        self.assertEqual(
            json.loads(response.content), {'email': ['Enter a valid email address.']})

    def test_create_customer_invalid_post_incorrect_phone(self):
        """
        Ensure phone number must have the right format '(XX) XXXXX-XXXX'
        """
        data = create_customer_data(phone='(11) 992745052')
        response = self.client.post(self.url, data)
        self.assertEqual(
            json.loads(response.content),
            {'phone': ["Phone number must have this format '(xx) xxxxx-xxxx'."]})

    def test_create_customer_invalid_post_incorrect_age(self):
        data = create_customer_data(age='@')
        response = self.client.post(self.url, data)
        self.assertEqual(
            json.loads(response.content), {'age': ["A valid integer is required."]})


class CustomerListTest(APITestCase):
    def setUp(self):
        self.url = reverse('customer-list')

    def test_get_customer_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_customer_with_empty_data(self):
        response = self.client.get(self.url)
        self.assertEqual(response.data['results'], [])

    def test_get_customer(self):
        data = create_customer_data()
        customer = Customer.objects.create(**data)
        response = self.client.get(self.url)

        self.assertDictContainsSubset(
            data, json.loads(response.content)['results'][0])


class CustomerDeleteTest(APITestCase):
    def setUp(self):
        data = create_customer_data()
        customer = Customer.objects.create(**data)
        self.url = reverse('customer-detail', kwargs={'pk': customer.pk})

    def test_delete_customer(self):
        response = self.client.delete(self.url)
        self.assertEqual(Customer.objects.count(), 0)
