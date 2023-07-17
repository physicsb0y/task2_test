from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(JobPost)
admin.site.register(JobRequirements)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(JobApplication)