# Generated by Django 4.2.5 on 2024-03-20 11:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0016_alter_jobsmodel_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsmodel',
            name='salary',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)]),
        ),
    ]
