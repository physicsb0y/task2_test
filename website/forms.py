from django import forms
from .models import JobPost, Blog, JobApplication
from . import models

from django_select2 import forms as s2forms




class RequirementsWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        'requirement__icontains'
    ]



class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['title', 'description', 'location', 'salary', 'job_type', 'position', 'category', 'requirements']
        widgets = {
            "requirements": RequirementsWidget
        }


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'content']


class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)



class JobSearchForm(forms.Form):
    # LOCATION_CHOICES = (
    #     ('kathmandu', 'Kathmandu'),
    #     ('lalitpur', 'Lalitpur'),
    #     ('bhaktapur', 'Bhaktapur'),
    #     ('pokhara', 'Pokhara'),
    #     ('dharan', 'Dharan')
    # )

    job_search_query = forms.CharField(required=False, max_length=100)
    search_area = forms.CharField(required=False, max_length=100)
    min_salary = forms.IntegerField(required=False)
    max_salary = forms.IntegerField(required=False)
    job_type = forms.CharField(required=False)
    position = forms.CharField(required=False)
    category = forms.CharField(required=False)



class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['first_name', 'last_name', 'email', 'address', 'cv', 'about_yourself']


