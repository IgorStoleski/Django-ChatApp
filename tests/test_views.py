from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestViewCase(TestCase):

    def setUp(self):
        # Hier könnten Sie einen User für die login_required Views erstellen
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.welcome_url = reverse('welcome')

    def test_welcome_view(self):
        # Test, ob die welcome_view die richtige Seite rendert
        response = self.client.get(self.welcome_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/welcome.html')

    def test_index_view_without_login(self):
        # Test für index_view ohne Login, sollte redirecten
        index_url = reverse('index')  # Verwenden Sie den Namen der URL aus Ihrer urls.py
        response = self.client.get(index_url)
        self.assertEqual(response.status_code, 302)  # 302 ist der Statuscode für Redirect

    def test_index_view_with_login(self):
        # Test für index_view mit Login
        self.client.login(username='testuser', password='12345')
        index_url = reverse('index')  # Verwenden Sie den Namen der URL aus Ihrer urls.py
        response = self.client.get(index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/index.html')