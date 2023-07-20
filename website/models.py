from django.db import models
from accounts.models import CustomUser
from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Location(models.Model):
    location_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.location_name



class Category(models.Model):
    category = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.category



class JobPost(models.Model):
    JOB_TYPE_CHOICES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('remote', 'Remote')
    )

    POSITION_TYPE_CHOICES = (
        ('intern', 'Intern'),
        ('junior', 'Junior'),
        ('intermediate', 'Intermediate'),
        ('professional', 'Professional')
    )

    
    employer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = RichTextUploadingField()
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    position = models.CharField(max_length=55, choices=POSITION_TYPE_CHOICES)
    salary = models.IntegerField()
    job_type = models.CharField(max_length=100, choices=JOB_TYPE_CHOICES)
    is_open = models.BooleanField(default=True)
    requirements = models.ManyToManyField('JobRequirements')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class JobRequirements(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    requirement = models.CharField(max_length=255)

    def __str__(self):
        return self.requirement


class Blog(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hashtags = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
    


class JobApplication(models.Model):
    GENDER_CHOICE_FIELDS = (
        ('female', 'Female'),
        ('male', 'Male'),
        ('other', 'Other')
    )

    post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    cv = models.FileField(upload_to='Resumes/')
    about_yourself = models.TextField()
    education_qualification = models.CharField(max_length=500)
    experience_in_years = models.IntegerField(null=True, blank=True)
    company = models.CharField(max_length=500, null=True, blank=True)
    company_phone = models.CharField(null=True, blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICE_FIELDS)
    dob = models.DateField()


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.post.title}"