from django import forms
from .models import JobPost, Blog, JobApplication, Location, Category
from . import models
from django.forms import widgets

from django_select2 import forms as s2forms
from django_select2.forms import ModelSelect2Mixin, HeavySelect2Widget, Select2MultipleWidget




class RequirementsWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        'requirement__icontains'
    ]

class CategoryWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        'category__icontains'
    ]


class LocationWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        'location_name__icontains'
    ]



class JobPostForm(forms.ModelForm):
    # my_field = forms.ModelChoiceField(
    #     queryset = Location.objects.all(),
    #     widget = HeavySelect2Widget(
    #         data_view = 'my-autocomplete-view',
    #         attrs={'data-minimum-input-length: 0'}
    #     )
    # )
    class Meta:
        model = JobPost
        fields = ['title', 'description', 'location', 'salary', 'job_type', 'position', 'category', 'requirements']
        widgets = {
            "requirements": RequirementsWidget,
            "location": LocationWidget,
            "category": CategoryWidget
        }


# class HashtagWidget(s2forms.ModelSelect2MultipleWidget):
#     hashtags = forms.CharField(widget=Select2MultipleWidget(
#         attrs={'multiple': 'multiple'}
#     ))

class CustomHashtagWidget(Select2MultipleWidget):
    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        attrs['data-tags'] = 'true'
        return attrs


class BlogPostForm(forms.ModelForm):
    hashtags = forms.CharField(
        widget=CustomHashtagWidget(attrs={'multiple': 'multiple'})
    )

    class Meta:
        model = Blog
        fields = ['title', 'category', 'content', 'hashtags']
        
    

class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'content', 'hashtags']



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
        fields = ['first_name', 'last_name', 'gender', 'email', 'address', 'dob', 'cv', 'experience_in_years', 'company', 'company_phone', 'education_qualification', 'about_yourself']
        widgets = {
            'dob': widgets.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
        }


