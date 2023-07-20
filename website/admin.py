from django.contrib import admin
from .models import *

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    fields = ['title', 'hashtags', 'author']



admin.site.register(JobPost)
admin.site.register(JobRequirements)
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(JobApplication)
admin.site.register(Location)