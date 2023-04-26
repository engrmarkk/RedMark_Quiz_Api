from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from ..models import User, UserProfile, Question


class QuestionTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser",
                                             first_name="testfirstname",
                                             last_name="testlastname",
                                             email="test@email.com",
                                             password="testpassword")
        UserProfile.objects.create(user=self.user)
        self.token = Token.objects.create(user=self.user)
        self.question = Question.objects.create(question_text="test question")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_all_questions(self):
        url = reverse('question')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_question(self):
        url = reverse('question')
        data = {
            "question_text": "test question2"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['question_text'], 'test question2')

    def test_get_each_question(self):
        url = reverse("each_question", args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['question_text'], 'test question')

    def test_update_each_question(self):
        url = reverse("each_question", args=[1])
        data = {
            "question_text": "test question updated"
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['question_text'], 'test question updated')
