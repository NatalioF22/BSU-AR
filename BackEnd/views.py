

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import transaction
import traceback
from django.http import HttpResponse
from .models import Department, Subject, Roadmap, Professor
from .forms import DepartmentForm, SubjectForm, RoadmapForm, ProfessorForm

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Only authorized personnel can log in.")
    return render(request, 'backend/login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard View
@login_required(login_url='login')
def dashboard(request):
    context = {
        'departments': Department.objects.all(),
        'subjects': Subject.objects.all(),
        'professors': Professor.objects.all(),
        'roadmaps': Roadmap.objects.all(),
    }
    return render(request, 'backend/dashboard.html', context)

# Professors View (List & Create)
@login_required(login_url='login')
def professors(request):
    form = ProfessorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('professors')
    context = {
        'professors': Professor.objects.all(),
        'form': form
    }
    return render(request, 'backend/professors.html', context)

# Single Professor View (Update/Delete)
@login_required(login_url='login')
def professor_detail(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    form = ProfessorForm(request.POST or None, request.FILES or None, instance=professor)
    if form.is_valid():
        form.save()
        return redirect('professors')
    context = {
        'professor': professor,
        'form': form
    }
    return render(request, 'backend/professor.html', context)

# Subjects View
@login_required(login_url='login')
def subjects(request):
    form = SubjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('subjects')
    context = {
        'subjects': Subject.objects.all(),
        'form': form
    }
    return render(request, 'backend/subjects.html', context)

# Single Subject View
# Update the subject_detail view in views.py to include roadmap information

@login_required(login_url='login')
def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    form = SubjectForm(request.POST or None, instance=subject)
    
    if form.is_valid():
        form.save()
        messages.success(request, f'Subject "{subject.name}" updated successfully.')
        return redirect('subjects')
    
    # Find roadmaps that include this subject and determine the semester
    roadmaps = []
    for i in range(1, 9):
        semester_key = f'semester{i}'
        for roadmap in Roadmap.objects.filter(**{f'{semester_key}__in': [subject]}):
            roadmaps.append({
                'name': roadmap.name,
                'id': roadmap.id,
                'semester_number': i
            })
    
    context = {
        'subject': subject,
        'form': form,
        'roadmaps': roadmaps
    }
    
    return render(request, 'backend/subject.html', context)

# Roadmaps View
@login_required(login_url='login')
def roadmaps(request):
    form = RoadmapForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('roadmaps')
    context = {
        'roadmaps': Roadmap.objects.all(),
        'form': form
    }
    return render(request, 'backend/roadmaps.html', context)

# Single Roadmap View@login_required(login_url='login')
# Modified roadmap_detail view in views.py

# Updated roadmap_detail view in views.py

@login_required(login_url='login')
def roadmap_detail(request, pk):
    roadmap = get_object_or_404(Roadmap, pk=pk)
    
    if request.method == 'POST':
        print("Form submitted with data:", request.POST)
        
        # Simplified approach - only save basic fields
        try:
            # Update basic fields manually
            roadmap.name = request.POST.get('name', roadmap.name)
            
            # Update department if provided
            department_id = request.POST.get('department')
            if department_id:
                try:
                    department = Department.objects.get(id=department_id)
                    roadmap.department = department
                except Department.DoesNotExist:
                    pass
            
            # Handle poster file if uploaded
            if 'poster' in request.FILES:
                roadmap.poster = request.FILES['poster']
            
            # Save basic fields
            roadmap.save()
            
            # Clear and update semesters one by one
            for i in range(1, 9):
                semester_key = f'semester{i}'
                subject_ids = request.POST.getlist(semester_key)
                
                # Get the semester manager
                semester = getattr(roadmap, semester_key)
                
                # Clear all existing subjects
                semester.clear()
                
                # Add new subjects if any
                if subject_ids:
                    valid_ids = []
                    for id_str in subject_ids:
                        try:
                            valid_ids.append(int(id_str))
                        except (ValueError, TypeError):
                            continue
                    
                    if valid_ids:
                        subjects = Subject.objects.filter(id__in=valid_ids)
                        for subject in subjects:
                            semester.add(subject)
            
            messages.success(request, 'Roadmap updated successfully!')
            return redirect('roadmaps')
        
        except Exception as e:
            print(f"Error: {e}")
            messages.error(request, f'Error: {e}')
    
    # Prepare semesters data for template
    semesters = [
        ('semester1', 'Semester 1', roadmap.semester1.all()),
        ('semester2', 'Semester 2', roadmap.semester2.all()),
        ('semester3', 'Semester 3', roadmap.semester3.all()),
        ('semester4', 'Semester 4', roadmap.semester4.all()),
        ('semester5', 'Semester 5', roadmap.semester5.all()),
        ('semester6', 'Semester 6', roadmap.semester6.all()),
        ('semester7', 'Semester 7', roadmap.semester7.all()),
        ('semester8', 'Semester 8', roadmap.semester8.all()),
    ]
    
    # Create a form for the template
    form = RoadmapForm(instance=roadmap)
    
    context = {
        'roadmap': roadmap,
        'form': form,
        'semesters': semesters,
        'all_subjects': Subject.objects.all()
    }
    
    return render(request, 'backend/roadmap.html', context)
# Departments View
@login_required(login_url='login')
def departments(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('departments')
    context = {
        'departments': Department.objects.all(),
        'form': form
    }
    return render(request, 'backend/departments.html', context)

# Single Department View
@login_required(login_url='login')
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    form = DepartmentForm(request.POST or None, instance=department)
    if form.is_valid():
        form.save()
        return redirect('departments')
    context = {
        'department': department,
        'form': form
    }
    return render(request, 'backend/department.html', context)

@login_required(login_url='login')
def delete_roadmap(request, pk):
    roadmap = get_object_or_404(Roadmap, pk=pk)
    if request.method == 'POST':
        roadmap.delete()
        return redirect('roadmaps')


@login_required(login_url='login')
def add_roadmap(request):
    form = RoadmapForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('roadmaps')
    return render(request, 'backend/addRoadmap.html', {'form': form})

@login_required(login_url='login')
def add_professor(request):
    form = ProfessorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('professors')
    return render(request, 'backend/addProfessor.html', {'form': form})

@login_required(login_url='login')
def add_department(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('departments')
    return render(request, 'backend/addDepartment.html', {'form': form})

@login_required(login_url='login')
def add_subject(request):
    form = SubjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('subjects')
    return render(request, 'backend/addSubject.html', {'form': form})


@login_required(login_url='login')
def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        name = department.name  # Store name before deletion for message
        try:
            department.delete()
            messages.success(request, f'Department "{name}" has been deleted successfully.')
        except Exception as e:
            messages.error(request, f'Error deleting department: {str(e)}')
        return redirect('departments')

@login_required(login_url='login')
def delete_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method == 'POST':
        name = professor.name  # Store name before deletion for message
        try:
            professor.delete()
            messages.success(request, f'Professor "{name}" has been deleted successfully.')
        except Exception as e:
            messages.error(request, f'Error deleting professor: {str(e)}')
        return redirect('professors')

@login_required(login_url='login')
def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        name = f"{subject.name} - {subject.title}"  # Store name before deletion for message
        try:
            subject.delete()
            messages.success(request, f'Subject "{name}" has been deleted successfully.')
        except Exception as e:
            messages.error(request, f'Error deleting subject: {str(e)}')
        return redirect('subjects')