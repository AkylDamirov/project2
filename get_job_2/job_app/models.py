from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.



class JobsModel(models.Model):
    image = models.ImageField(upload_to='my_data')
    company_name = models.CharField(max_length=50)
    description = models.TextField(max_length=3000)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    salary = models.IntegerField(validators=[MaxValueValidator(999999)])
    date = models.DateTimeField(auto_now_add=True)
    work_position = models.CharField(max_length=40)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=150)


    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        if self.country:
            self.country = self.country.title()
        super().save(*args, **kwargs)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(JobsModel, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart for {self.user.username} | Job {self.product}'




