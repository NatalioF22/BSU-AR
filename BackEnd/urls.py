"""
URL configuration for Core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py
from django.urls import path
from . import views

urlpatterns = [
# Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    
    # Professors
    path('backend/professors/', views.professors, name='professors'),
    path('backend/professors/<int:pk>/', views.professor_detail, name='professor_detail'),
    
    # Subjects
    path('backend/subjects/', views.subjects, name='subjects'),
    path('backend/subjects/<int:pk>/', views.subject_detail, name='subject_detail'),
    
    # Roadmaps
    path('backend/roadmaps/', views.roadmaps, name='roadmaps'),
    path('backend/roadmaps/delete/<int:pk>/', views.delete_roadmap, name='delete_roadmap'),

    path('backend/roadmaps/<int:pk>/', views.roadmap_detail, name='roadmap_detail'),
    
    # Departments
    path('backend/departments/', views.departments, name='departments'),
    path('backend/departments/<int:pk>/', views.department_detail, name='department_detail'),

    path('backend/add-roadmap/', views.add_roadmap, name='add_roadmap'),
    path('backend/add-professor/', views.add_professor, name='add_professor'),
    path('backend/add-department/', views.add_department, name='add_department'),
    path('backend/add-subject/', views.add_subject, name='add_subject'),

     # Delete URLs
    path('backend/departments/delete/<int:pk>/', views.delete_department, name='delete_department'),
    path('backend/professors/delete/<int:pk>/', views.delete_professor, name='delete_professor'),
    path('backend/subjects/delete/<int:pk>/', views.delete_subject, name='delete_subject'),
]