from django.test import TestCase, Client
from django.urls import reverse
from job_app.models import JobsModel, Cart
from django.contrib.auth.models import User
import json
from django.http import HttpResponseRedirect, Http404
#
# test_user = User.objects.get(username='test_user')

class TestViews(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(username='test', password='password123')
        self.client = Client()
        self.job = JobsModel.objects.create(
            company_name = 'test',
            description = 'test',
            salary = 1,
            work_position = 'test',
            phone_number = '1111111',
            email = 'test@gmail.com',
            creator = User.objects.get(username='test'),
            image = 'uploads/ebay.png'
        )
        self.list_url = reverse('home')
        self.about_url = reverse('about', args=[self.job.pk])
        self.add_vacancy_url = reverse('add_vacancy')
        self.delete_profile_url = reverse('delete2', args=[self.job.pk])

    def test_index_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'job_app/index.html')

    def test_about_GET(self):
        response = self.client.get(self.about_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'job_app/about.html')

    def test_add_vacancy_POST(self):
        form_data = {
            'company_name': 'test',
            'description': 'test',
            'salary': 1,
            'work_position': 'test',
            'phone_number': '11111111',
            'email': 'test@example.com',
            'image': 'uploads/new_image.png'
        }
        response = self.client.post(self.add_vacancy_url, form_data)
        self.assertEqual(response.status_code, 302)

        new_job = JobsModel.objects.get(company_name='test')
        self.assertIsNotNone(new_job)

    def test_add_vacancy_nodata_POST(self):
        response = self.client.post(self.add_vacancy_url)
        self.assertEqual(response.status_code, 302)

        new_job = JobsModel.objects.get(company_name='test')
        self.assertIsNotNone(new_job)

    def test_DELETE_vacancy(self):
        response = self.client.delete(self.delete_profile_url)
        self.assertIsInstance(response, HttpResponseRedirect)

        with self.assertRaises(JobsModel.DoesNotExist):
            JobsModel.objects.get(pk=self.job.pk)

    # def test_profile_delete_no_id(self):
    #     response = self.client.delete(self.delete_profile_url)
    #     self.assertEqual(response.status_code, 404)
