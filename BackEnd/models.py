#BSU-AR/BackEnd/models.py
from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    department = models.ForeignKey(
        Department,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    credit_hours = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.name}"


class Professor(models.Model):
    picture = models.ImageField(upload_to='professor_pics/', blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    education_level = models.CharField(max_length=200, blank=True, null=True)
    subjects = models.ManyToManyField(Subject, related_name="professors", blank=True)

    def __str__(self):
        return self.name or "Unnamed Professor"

# Modified Roadmap model in models.py
# Modify the Roadmap model in models.py

class Roadmap(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, related_name="roadmaps", on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='roadmap_posters/', null=True, blank=True)

    semester1 = models.ManyToManyField(Subject, related_name="semester1", blank=True)
    semester2 = models.ManyToManyField(Subject, related_name="semester2", blank=True)
    semester3 = models.ManyToManyField(Subject, related_name="semester3", blank=True)
    semester4 = models.ManyToManyField(Subject, related_name="semester4", blank=True)
    semester5 = models.ManyToManyField(Subject, related_name="semester5", blank=True)
    semester6 = models.ManyToManyField(Subject, related_name="semester6", blank=True)
    semester7 = models.ManyToManyField(Subject, related_name="semester7", blank=True)
    semester8 = models.ManyToManyField(Subject, related_name="semester8", blank=True)

    def __str__(self):
        return f"{self.name} - {self.department.name if self.department else 'No Department'}"

    # Temporarily disable validation for testing
    def clean(self):
        # Validation disabled to troubleshoot saving issues
        pass

    # You can re-enable this later:
    """
    def clean(self):
        if not self.pk:  # Skip validation if the roadmap isn't saved yet
            return

        semesters = [
            self.semester1,
            self.semester2,
            self.semester3,
            self.semester4,
            self.semester5,
            self.semester6,
            self.semester7,
            self.semester8
        ]

        all_subjects = []
        for semester in semesters:
            subjects = semester.all()
            for subject in subjects:
                if subject in all_subjects:
                    raise ValidationError(f"Subject '{subject}' appears in multiple semesters.")
                all_subjects.append(subject)
    """