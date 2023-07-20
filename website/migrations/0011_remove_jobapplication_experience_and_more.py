# Generated by Django 4.2.2 on 2023-07-19 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_jobapplication_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='experience',
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='company',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='company_phone',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='experience_in_years',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male'), ('other', 'Other')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='education_qualification',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
