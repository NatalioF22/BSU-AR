from django import forms
from .models import Department, Subject, Roadmap, Professor

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department Name'})
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'title', 'department', 'credit_hours', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject Name'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject Title'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'credit_hours': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Credit Hours'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
        }

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['picture', 'name', 'education_level', 'subjects']
        widgets = {
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Professor Name'}),
            'education_level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Education Level'}),
            'subjects': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }

# Modified RoadmapForm that doesn't include semester fields
class RoadmapForm(forms.ModelForm):
    class Meta:
        model = Roadmap
        fields = ['name', 'department', 'poster']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'poster': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }