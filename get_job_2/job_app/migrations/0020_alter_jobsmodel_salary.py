# Generated by Django 4.2.5 on 2024-03-21 11:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0019_alter_jobsmodel_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsmodel',
            name='salary',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(7)]),
        ),
    ]
