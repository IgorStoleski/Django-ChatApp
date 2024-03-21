from django.test import SimpleTestCase
from django.urls import reverse, resolve
from chat.views import index, login_view, logout_view, welcome_view, register_view


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