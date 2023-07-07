from django.contrib.auth.models import User, AbstractUser, Group, Permission
from django.db import models
from pathlib import Path

def user_directory_path(instance, filename):
    username = instance.username
    if filename == 'defaultpp.jpg':
        return f"profile_pictures/{username}/default.jpg"
    return f"profile_pictures/{username}/{filename}"



class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('employer', 'Employer'),
        ('admin_staff', 'Admin/Staff')
    )

    user_type = models.CharField(max_length=35, choices=USER_TYPE_CHOICES)
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True, default='defaultpp.jpg')
    phone = models.IntegerField(blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_users'  # Add a custom related name
    )
               
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_users'  # Add a custom related name
    )


