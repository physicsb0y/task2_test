from django import forms

from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class JobSeekerForm(UserCreationForm):
    USER_TYPE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('employer', 'Employer'),
        ('admin_staff', 'Admin/Staff')
    )

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, initial='job_seeker', disabled=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'image', 'email', 'phone', 'password1', 'password2', 'user_type']


class EmployerForm(UserCreationForm):
    

    USER_TYPE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('employer', 'Employer'),
        ('admin_staff', 'Admin/Staff')
    )

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, initial='employer', disabled=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'image', 'email', 'phone', 'password1', 'password2', 'user_type']


class JobSeekerUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'image', 'email', 'phone']


class EmployerUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'image', 'email', 'phone']