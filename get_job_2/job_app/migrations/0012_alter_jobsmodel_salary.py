# Generated by Django 4.2.5 on 2024-03-18 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0011_jobsmodel_email_jobsmodel_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsmodel',
            name='salary',
            field=models.IntegerField(max_length=10),
        ),
    ]
