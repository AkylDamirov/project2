# Generated by Django 4.2.5 on 2023-12-30 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0005_alter_jobsmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsmodel',
            name='description',
            field=models.TextField(max_length=3000),
        ),
    ]
