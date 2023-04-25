from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from ..models import User, UserProfile


class UserTests(APITestCase):
    def SetUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser",
                                             first_name="testfirstname",
                                             last_name="testlastname",
                                             email="test@email.com",
                                             password="testpassword")
        self.token = Token.objects.create(user=self.user)

    def test_get_all_users(self):
        url = reverse('all users')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
