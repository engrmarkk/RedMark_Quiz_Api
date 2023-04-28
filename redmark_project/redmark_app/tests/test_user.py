from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from ..models import User, UserProfile


class UserTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser",
                                             first_name="testfirstname",
                                             last_name="testlastname",
                                             email="test@email.com",
                                             password="testpassword")
        UserProfile.objects.create(user=self.user)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_all_users(self):
        url = reverse('all users')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_each_user(self):
        url = reverse("each user", args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['first_name'], 'testfirstname')

    def test_register_user(self):
        url = reverse('register')
        data = {
            "username": "testregistration",
            "first_name": "testfirstname",
            "last_name": "testlastname",
            "email": "testreg@email.com",
            "password": "Testpassword1"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
