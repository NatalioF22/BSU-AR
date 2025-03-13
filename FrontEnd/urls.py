# Update your URLs for frontend routes 
from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    
    # Frontend (public) routes
    path('', views.index, name='index'),
    path('departments/', views.public_departments, name='public_departments'),
    path('departments/<int:pk>/', views.public_department_detail, name='public_department_detail'),
    path('subjects/', views.public_subjects, name='public_subjects'),
    path('subjects/<int:pk>/', views.public_subject_detail, name='public_subject_detail'),
    path('roadmaps/', views.public_roadmaps, name='public_roadmaps'),
    path('roadmaps/<int:pk>/', views.public_roadmap_detail, name='public_roadmap_detail'),
    path('professors/', views.public_professors, name='public_professors'),
    path('professors/<int:pk>/', views.public_professor_detail, name='public_professor_detail'),
    
]