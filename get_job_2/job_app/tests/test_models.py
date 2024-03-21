from django.test import TestCase
from django.contrib.auth.models import User
from job_app.models import JobsModel

class JobsModelTest(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(username='test', password='password1234')
        self.job = JobsModel.objects.create(
            company_name='test',
            description='test',
            salary=1,
            work_position='test',
            phone_number='1111111',
            email='test@gmail.com',
            creator=User.objects.get(username='test'),
            image='uploads/ebay.png'
        )

    def test_company_name_label(self):
        job = JobsModel.objects.get(id=self.job.id)
        field_label = job._meta.get_field('company_name').verbose_name
        self.assertEqual(field_label, 'company name')

    def test_salary_max_length(self):
        job = JobsModel.objects.get(id=self.job.id)
        max_value = job._meta.get_field('salary').get_internal_type()
        self.assertEqual(max_value, 'IntegerField')

    def test_creator_relationship(self):
        job = JobsModel.objects.get(id=self.job.id)
        self.assertEqual(job.creator.username, 'test')












