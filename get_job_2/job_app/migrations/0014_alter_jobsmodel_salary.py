# Generated by Django 4.2.5 on 2024-03-20 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0013_alter_jobsmodel_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsmodel',
            name='salary',
            field=models.DecimalField(decimal_places=0, max_digits=19),
        ),
    ]
