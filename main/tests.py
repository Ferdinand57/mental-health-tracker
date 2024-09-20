from django.test import TestCase, Client
from django.utils import timezone
from .models import MoodEntry
from django.contrib.auth.models import User

class MainTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')
        # Set the last_login cookie
        self.client.cookies['last_login'] = '2024-09-20 12:00:00'  # Example timestamp

    def test_main_url_is_exist(self):
        # Use self.client instead of Client()
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        # Use self.client instead of Client()
        response = self.client.get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        # Use self.client instead of Client()
        response = self.client.get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_strong_mood_user(self):
        now = timezone.now()
        mood = MoodEntry.objects.create(
          mood="Happy",
          time=now,
          feelings="I'm happy, even though my clothes are soaked from the rain :(",
          mood_intensity=8,
          user=self.user  # Associate the mood entry with the test user
        )
        self.assertEqual(mood.user.username, 'testuser')
        self.assertTrue(mood.is_mood_strong)

    def test_main_template_uses_correct_page_title(self): 
        response = self.client.get("/")
        html_response = response.content.decode("utf8")
        self.assertIn("PBD Mental Health Tracker", html_response)