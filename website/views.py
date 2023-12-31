from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import JobPostSerializer

from accounts.models import CustomUser
from .forms import JobPostForm, BlogPostForm, BlogUpdateForm, SearchForm, JobSearchForm, JobApplicationForm
from .models import JobPost, Blog, Category, JobApplication, Location

# Create your views here.

class IndexView(ListView):
    model = CustomUser
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = CustomUser.objects.all()
        categories = Category.objects.all()
        locations = Location.objects.all()
        context["users"] = users
        context["categories"] = categories
        context['locations'] = locations
        return context
    


class AboutView(ListView):
    model = CustomUser
    template_name = 'website/about.html'



@method_decorator(login_required, name='dispatch')
class JobPostView(CreateView):
    form_class = JobPostForm
    template_name = 'website/jobpost.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.employer = self.request.user
        response = super().form_valid(form)
        return response

class JobListView(ListView):
    model = JobPost
    template_name = 'website/joblist.html'

    def get(self, request):
        job_posts = JobPost.objects.all()
        unique_locations = Location.objects.all()
        unique_job_type = set(JobPost.objects.values_list('job_type', flat=True))
        unique_position = set(JobPost.objects.values_list('position', flat=True))
        unique_category = Category.objects.all()

        context = {
            'job_posts': job_posts,
            'unique_locations': unique_locations,
            'unique_job_type': unique_job_type,
            'unique_position': unique_position,
            'unique_category': unique_category
        }
        return render(request, 'website/joblist.html', context)



class JobDescriptionView(DetailView):
    model = JobPost
    template_name = 'website/jobdescription.html'
    context_object_name = 'job_post'



@method_decorator(login_required, name='dispatch')
class BlogCreateView(CreateView):
    form_class = BlogPostForm
    template_name = 'website/create_blog.html'
    success_url = reverse_lazy('blog_page')

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return response
    

class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogUpdateForm
    template_name = 'website/blogupdate.html'
    success_url = reverse_lazy('blog_page')

    def form_valid(self, form):
        return super().form_valid(form)



class BlogPage(ListView):
    model = Blog
    template_name = 'website/blog_page.html'
    context_object_name = 'blogs'


class SingleBlogView(DetailView):
    model = Blog
    template_name = 'website/single_blog.html'
    context_object_name = 'blog'


def contact(request):
    return render(request, 'website/contact.html')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('index')



class SearchView(View):
    def get(self, request):
        form = SearchForm(request.GET or None)
        search_query = None
        results = None

        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            blog_results = Blog.objects.filter(title__icontains=search_query)
            job_results = JobPost.objects.filter(title__icontains=search_query)

            context = {
                'form': form,
                'search_query': search_query,
                'blog_results': blog_results,
                'job_results': job_results
            }

            return render(request, 'website/search.html', context)
        


class JobSearchView(ListView):
    model = JobPost
    template_name = 'website/joblist.html'
    context_object_name = 'job_posts'

    def get(self, request):
        form = JobSearchForm(request.GET or None)
        job_posts = JobPost.objects.all()
        

        # job_search_query = None
        # search_area = None
        # min_salary = None
        # max_salary = None
        # job_type = None
        # position = None
        # category = None
        results = None

        if form.is_valid():
            job_search_query = form.cleaned_data.get('job_search_query')
            search_area = form.cleaned_data.get('search_area')
            min_salary = form.cleaned_data.get('min_salary')
            max_salary = form.cleaned_data.get('max_salary')
            job_type = form.cleaned_data.get('job_type')
            position = form.cleaned_data.get('position')
            category = form.cleaned_data.get('category')

            

            results = job_posts
            

            if job_search_query:
                results = results.filter(title__icontains=job_search_query)

            if search_area:
                results = results.filter(location__location_name__icontains=search_area)

            if min_salary and max_salary:
                results = results.filter(salary__range=(min_salary, max_salary))

            if min_salary:
                results = results.filter(salary__gte=min_salary)

            if max_salary:
                results = results.filter(salary__lte=max_salary)

            if job_type:
                results = results.filter(job_type__icontains=job_type)

            if position:
                results = results.filter(position__icontains=position)

            if category:
                results = results.filter(category__category__icontains=category)

            unique_locations = Location.objects.all()
            unique_job_type = set(JobPost.objects.values_list('job_type', flat=True))
            unique_position = set(JobPost.objects.values_list('position', flat=True))
            unique_category = Category.objects.all()

            context = {
                'form': form,
                'job_search_query': job_search_query,
                'search_area': search_area,
                'min_salary': min_salary,
                'max_salary': max_salary,
                'job_type': job_type,
                'position': position,
                'category': category,
                'results': results,
                'job_posts': job_posts,
                'unique_location': unique_locations,
                'unique_job_type': unique_job_type,
                'unique_position': unique_position,
                'unique_category': unique_category
            }

            return render(request, 'website/jobsearch.html', context)
       


class JobApplicationView(LoginRequiredMixin, CreateView):
    model = JobApplication
    form_class = JobApplicationForm
    template_name = 'website/job_apply.html'
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        self.job_post = get_object_or_404(JobPost, id=self.kwargs['pk'])
        return super().get(request, *args, **kwargs)


    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user
        initial['first_name'] = user.first_name
        initial['last_name'] = user.last_name
        initial['email'] = user.email
        return initial


    def form_valid(self, form):
        job_post_id = self.kwargs['pk']
        job_post = get_object_or_404(JobPost, id=job_post_id)

        form.instance.post = job_post
        response = super().form_valid(form)
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["job_post_id"] = self.kwargs['pk']
        return context
    


class CategoryJobsView(ListView):
    template_name = 'website/category_jobs.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return JobPost.objects.filter(category_id=category_id)
    


#==========================API=====================


class JobPostApiView(APIView):
    @login_required
    def get(self, request):
        models = JobPost.objects.all()
        return Response(models.values())