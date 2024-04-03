from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

# class Customer(models.Model):
#     user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name

# class User(models.Model):
#     username = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)



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
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)
    # , default = User.objects.get(username='admin')

    # customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)

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

# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False)
#     transaction_id = models.CharField(max_length=100, null=True)
#
#     def __str__(self):
#         return str(self.id)
#
# class OrderItem(models.Model):
#     product = models.ForeignKey(JobsModel, on_delete=models.SET_NULL, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#     #
#     image = models.ImageField()
#     company_name = models.CharField(max_length=50)
#     description = models.TextField(max_length=400)
#     salary = models.IntegerField()
#     date = models.DateTimeField(default=timezone.now)
#     work_position = models.CharField(max_length=40)


