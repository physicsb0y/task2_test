# Generated by Django 4.2.2 on 2023-07-19 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_jobapplication_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='dob',
            field=models.DateField(),
        ),
    ]
