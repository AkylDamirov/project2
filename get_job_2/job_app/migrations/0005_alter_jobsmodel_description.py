# Generated by Django 4.2.5 on 2023-12-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0004_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsmodel',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]