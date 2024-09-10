from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class HelloWorldTests(APITestCase):
    def test_hello_world(self):
        url = reverse("hello_world")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, b'{"message":"Hello, World!"}')
