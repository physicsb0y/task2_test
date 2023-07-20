from django.urls import path

from .views import IndexView, AboutView, JobPostView, JobListView, JobDescriptionView, BlogCreateView, BlogPage, SingleBlogView, contact, SearchView, JobSearchView, JobApplicationView, CategoryJobsView, JobPostApiView, BlogDeleteView, BlogUpdateView



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('index', IndexView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('createjob', JobPostView.as_view(), name='create_job'),
    path('joblist/', JobListView.as_view(), name='job_list'),
    path('joblist/jobdescription/<int:pk>', JobDescriptionView.as_view(), name='job_detail'),
    path('jobapply/<int:pk>/', JobApplicationView.as_view(), name='apply_job'),
    path('api/posts/', JobPostApiView.as_view(), name='job_post_api'),
    path('blog', BlogPage.as_view(), name='blog_page'),
    path('blog/<int:pk>', SingleBlogView.as_view(), name='blog_content'),
    path('blog/update/<pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/blog_create', BlogCreateView.as_view(), name='create_blog'),
    path('delete/<pk>', BlogDeleteView.as_view(), name='blog_delete'),
    path('contact', contact, name='contact'),
    path('search/', SearchView.as_view(), name='search'),
    path('jobsearch', JobSearchView.as_view(), name='job_search'),
    path('category/<int:category_id>', CategoryJobsView.as_view(), name='category_jobs'),
]
