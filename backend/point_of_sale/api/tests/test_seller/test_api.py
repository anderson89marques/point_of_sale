"""Test suit for seller API"""
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from point_of_sale.api.models import Seller
from point_of_sale.api.tests import create_seller_data


class SellerValidPostTest(APITestCase):
    def setUp(self):
        self.url = reverse('seller-list')
        self.data = create_seller_data()
        self.response = self.client.post(self.url, self.data)

    def test_create_seller_status_code(self):
        """Response must have status_code 201 CREATED"""

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_create_seller(self):
        """There must be one seller"""
        self.assertEqual(Seller.objects.count(), 1)


class SellerNewPostInvalidTest(APITestCase):
    def setUp(self):
        self.url = reverse('seller-list')

    def test_create_seller_invalid_post_status_code(self):
        data = create_seller_data(name='Anderson Marques1')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_create_seller(self):
        self.assertEqual(Seller.objects.count(), 0)

    def test_create_seller_invalid_post_incorrect_name(self):
        data = create_seller_data(name='Anderson Marques1')
        response = self.client.post(self.url, data)
        self.assertEqual(json.loads(response.content), {
                         'name': ['Name should not contains digit.']})

    def test_create_seller_invalid_post_incorrect_email(self):
        data = create_seller_data(email='andersonoanjo18')
        response = self.client.post(self.url, data)
        self.assertEqual(json.loads(response.content), {
                         'email': ['Enter a valid email address.']})

    def test_create_seller_invalid_post_incorrect_phone(self):
        """
        Ensure phone number must have the right format '(XX) XXXXX-XXXX'
        """
        data = create_seller_data(phone='(11) 992745052')
        response = self.client.post(self.url, data)
        self.assertEqual(json.loads(response.content), {
                         'phone': ["Phone number must have this format '(xx) xxxxx-xxxx'."]})
    
    def test_create_seller_invalid_post_incorrect_age(self):
        data = create_seller_data(age='@')
        response = self.client.post(self.url, data)
        self.assertEqual(json.loads(response.content), {
                         'age': ["A valid integer is required."]})


class SellerListTest(APITestCase):
    def setUp(self):
        self.url = reverse('seller-list')

    def test_get_seller_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_seller_with_empty_data(self):
        response = self.client.get(self.url)
        self.assertEqual(response.data['results'], [])

    def test_get_seller(self):
        data = create_seller_data()
        seller = Seller.objects.create(**data)
        response = self.client.get(self.url)
        self.assertDictContainsSubset(
            data, json.loads(response.content)['results'][0])


class SellerDeleteTest(APITestCase):
    def setUp(self):
        data = create_seller_data()
        seller = Seller.objects.create(**data)
        self.url = reverse('seller-detail', kwargs={'pk': seller.pk})

    def test_delete_seller(self):
        response = self.client.delete(self.url)
        self.assertEqual(Seller.objects.count(), 0)