from django.urls import path, include

from .views import JobSeekerRegistrationView, EmployerRegistrationView, CustomLoginView, CustomLogoutView, CustomEmployeeUpdateView, CustomJobSeekerUpdateView, ProfileDetailView


urlpatterns = [
    path('accounts/jobseeker', JobSeekerRegistrationView.as_view(), name='j_registration'),
    path('accounts/employer', EmployerRegistrationView.as_view(), name='e_registration'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/update/<pk>', CustomEmployeeUpdateView.as_view(), name='employee_update'),
    path('accounts/update/<pk>', CustomJobSeekerUpdateView.as_view(), name='job_seeker_update'),
    path('accounts/update/<pk>', CustomJobSeekerUpdateView.as_view(), name='update'),
    path('accounts/profile/<pk>', ProfileDetailView.as_view(), name='profile'),
    path('accounts/logout', CustomLogoutView.as_view(), name='logout'),
    
]
