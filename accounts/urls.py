from django.urls import path, include

from .views import JobSeekerRegistrationView, EmployerRegistrationView, CustomLoginView, CustomLogoutView



urlpatterns = [
    path('accounts/jobseeker', JobSeekerRegistrationView.as_view(), name='j_registration'),
    path('accounts/employer', EmployerRegistrationView.as_view(), name='e_registration'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout', CustomLogoutView.as_view(), name='logout'),

]
