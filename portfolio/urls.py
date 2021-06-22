from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:project_id>/', views.single_project, name="single_project"),
    path('error/', views.error, name="error"),
    re_path(r'error/.+', views.error, name="error_bad_path"),
    re_path(r'projects/.*\D+', views.error, name="error_projects"),


    #path('about/', views.about, name="about")
]