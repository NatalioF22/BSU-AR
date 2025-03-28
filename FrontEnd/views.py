# Add these view functions to your views.py file
from django.shortcuts import render, get_object_or_404
from BackEnd.models import Department, Subject, Roadmap, Professor
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Frontend views (public, no login required)
def index(request):
    """Homepage view showing featured departments and roadmaps."""
    departments = Department.objects.all()
    roadmaps = Roadmap.objects.all()[:6]  # Limit to 6 recent roadmaps
    subjects = Subject.objects.all()[:8]  # Limit to 8 recent subjects
    professors = Professor.objects.all()[:4]  # Limit to 4 featured professors
    
    context = {
        'departments': departments,
        'roadmaps': roadmaps,
        'subjects': subjects,
        'professors': professors,
    }
    return render(request, 'index.html', context)

def public_departments(request):
    """View for public listing of all departments."""
    departments = Department.objects.all()
    
    context = {
        'departments': departments,
    }
    return render(request, 'frontend/departments.html', context)

def public_department_detail(request, pk):
    """View for public detail page of a single department."""
    department = get_object_or_404(Department, pk=pk)
    subjects = Subject.objects.filter(department=department)
    roadmaps = Roadmap.objects.filter(department=department)
    
    context = {
        'department': department,
        'subjects': subjects,
        'roadmaps': roadmaps,
    }
    return render(request, 'frontend/department_detail.html', context)



def public_subjects(request):
    """View for public listing of all subjects."""
    subjects_list = Subject.objects.all()
    departments = Department.objects.all()
    
    # Filter by department if provided
    department_id = request.GET.get('department')
    if department_id:
        try:
            department = Department.objects.get(id=department_id)
            subjects_list = subjects_list.filter(department=department)
        except Department.DoesNotExist:
            pass
    
    # Pagination - 50 items per page
    paginator = Paginator(subjects_list, 21)
    page = request.GET.get('page')
    
    try:
        subjects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        subjects = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        subjects = paginator.page(paginator.num_pages)
    
    context = {
        'subjects': subjects,
        'departments': departments,
        'selected_department': department_id,
    }
    return render(request, 'frontend/subjects.html', context)

def public_subject_detail(request, pk):
    """View for public detail page of a single subject."""
    subject = get_object_or_404(Subject, pk=pk)
    professors = subject.professors.all()
    
    # Find roadmaps that include this subject
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
        'professors': professors,
        'roadmaps': roadmaps,
    }
    return render(request, 'frontend/subject_detail.html', context)

def public_roadmaps(request):
    """View for public listing of all roadmaps."""
    roadmaps = Roadmap.objects.all()
    departments = Department.objects.all()
    
    # Filter by department if provided
    department_id = request.GET.get('department')
    if department_id:
        try:
            department = Department.objects.get(id=department_id)
            roadmaps = roadmaps.filter(department=department)
        except Department.DoesNotExist:
            pass
    
    context = {
        'roadmaps': roadmaps,
        'departments': departments,
        'selected_department': department_id,
    }
    return render(request, 'frontend/roadmaps.html', context)

def public_roadmap_detail(request, pk):
    """View for public detail page of a single roadmap."""
    roadmap = get_object_or_404(Roadmap, pk=pk)
    
    # Calculate credit totals
    year1_credits = sum(subject.credit_hours for subject in roadmap.semester1.all()) + \
                    sum(subject.credit_hours for subject in roadmap.semester2.all())
    
    year2_credits = sum(subject.credit_hours for subject in roadmap.semester3.all()) + \
                    sum(subject.credit_hours for subject in roadmap.semester4.all())
    
    year3_credits = sum(subject.credit_hours for subject in roadmap.semester5.all()) + \
                    sum(subject.credit_hours for subject in roadmap.semester6.all())
    
    year4_credits = sum(subject.credit_hours for subject in roadmap.semester7.all()) + \
                    sum(subject.credit_hours for subject in roadmap.semester8.all())
    
    total_credits = year1_credits + year2_credits + year3_credits + year4_credits
    
    semesters = [
        ('Semester 1', roadmap.semester1.all()),
        ('Semester 2', roadmap.semester2.all()),
        ('Semester 3', roadmap.semester3.all()),
        ('Semester 4', roadmap.semester4.all()),
        ('Semester 5', roadmap.semester5.all()),
        ('Semester 6', roadmap.semester6.all()),
        ('Semester 7', roadmap.semester7.all()),
        ('Semester 8', roadmap.semester8.all()),
    ]
    
    # Get other roadmaps from the same department
    other_roadmaps = Roadmap.objects.filter(department=roadmap.department).exclude(pk=roadmap.pk)
    
    context = {
        'roadmap': roadmap,
        'semesters': semesters,
        'other_roadmaps': other_roadmaps,
        'year1_credits': year1_credits,
        'year2_credits': year2_credits,
        'year3_credits': year3_credits,
        'year4_credits': year4_credits,
        'total_credits': total_credits,
    }
    
    return render(request, 'frontend/roadmap_detail.html', context)

def public_professors(request):
    """View for public listing of all professors."""
    professors = Professor.objects.all()
    
    context = {
        'professors': professors,
    }
    return render(request, 'frontend/professors.html', context)

def public_professor_detail(request, pk):
    """View for public detail page of a single professor."""
    professor = get_object_or_404(Professor, pk=pk)
    subjects = professor.subjects.all()
    
    context = {
        'professor': professor,
        'subjects': subjects,
    }
    return render(request, 'frontend/professor_detail.html', context)