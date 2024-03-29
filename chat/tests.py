""" from django.test import Client, TestCase
from django.contrib.auth.models import User

# Create your tests here.
class ChatTest(TestCase):
    def test_chatpage(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', password='testuser')
        self.client.login(username='testuser', password='testuser')
        response = self.client.get('/chat/')
        self.assertEqual(response.status_code, 200) """
        
        
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from chat.views import index, login_view, logout_view, welcome_view, register_view
from django.test import TestCase, Client
from django.contrib.auth.models import User



class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('welcome')
        self.assertEquals(resolve(url).func, welcome_view)
        
    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_view)
        
    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)
        
    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_view)
        
    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register_view)
        

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