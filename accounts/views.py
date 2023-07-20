from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate

from .models import CustomUser
from .forms import JobSeekerForm, EmployerForm, EmployerUpdateForm, JobSeekerUpdateForm

# Create your views here.

class JobSeekerRegistrationView(CreateView):
    form_class = JobSeekerForm
    template_name = 'accounts/registration/register.html'
    success_url = reverse_lazy('index')
    context_object_name = 'users'

    def form_valid(self, form):
        user = form.save()
        image = form.cleaned_data['image']
        user.image = image
        user.save()
        response = super().form_valid(form)
        return response
    
    def get_success_url(self):
        user = authenticate(user)
        return redirect('index')

class EmployerRegistrationView(CreateView):
    form_class = EmployerForm
    template_name = 'accounts/registration/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response



class CustomLoginView(LoginView):
    template_name = 'accounts/registration/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        user = self.request.user
        if user.user_type == 'job_seeker':
            return redirect('index')
        elif user.user_type == 'employer':
            return redirect('index')
        
        else:
            return redirect('index')
        
        return response

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')




class CustomEmployeeUpdateView(UpdateView):
    model = CustomUser
    template_name = "accounts/profile/updateprofile.html"
    form_class = EmployerUpdateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response



class CustomJobSeekerUpdateView(UpdateView):
    model = CustomUser
    template_name = "accounts/profile/updateprofile.html"
    form_class = JobSeekerUpdateForm
    success_url = reverse_lazy('index')

    def form_Valid(self, form):
        response = super().form_valid(form)
        return response





class ProfileDetailView(DetailView):
    model = CustomUser
    template_name = "accounts/profile/profiledetail.html"
    context_object_name = 'users'




