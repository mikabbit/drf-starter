from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthTestCase(APITestCase):

    def setUp(self):
        user = get_user_model().objects.create_user("user", "user@sample.com", "password")
        user.save()
    
    def test_auth(self):
        url = reverse("auth")
        data = {"username": "user", "password": "password"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)