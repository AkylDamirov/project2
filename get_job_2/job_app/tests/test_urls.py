from django.test import SimpleTestCase
from django.urls import reverse, resolve
from job_app.views import index, Vacancy, about

class TestUrls(SimpleTestCase):
    def test_home_url(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_add_url(self):
        url = reverse('add_vacancy')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, Vacancy)

    def test_about_url(self):
        url = reverse('about', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, about)