from django.test import SimpleTestCase,Client
from django.core.files.uploadedfile import SimpleUploadedFile
from job_app.forms import AddVacancy
from django.contrib.auth.models import User

class TestForms(SimpleTestCase):
    def test_add_vacancy_valid_data(self):
        with open('uploads/my_data/ebay.png', 'rb') as f:
            image_data = f.read()
        image_file = SimpleUploadedFile('ebay.png', image_data, content_type='image/png')
        form = AddVacancy(data={
            'company_name':'test',
            'work_position': 'test',
            'description':'test',
            'salary':1,
            'phone_number' : '1111111',
            'email' : 'test@gmail.com',
        }, files={'image': image_file})
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

 # 'creator' : User.objects.get(username='test'),
# User.objects.create_user(username='test', password='password123')
# Client().login(username='test', password='password123')