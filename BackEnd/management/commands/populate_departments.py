from django.core.management.base import BaseCommand
from BackEnd.models import *

class Command(BaseCommand):
    help = "Populate departments extracted from the PDF into the database."

    def handle(self, *args, **options):
        # List of departments extracted from the PDF
        departments = [
            "Accounting and Finance",
            "Actuarial Science",
            "African Studies",
            "African American Studies",
            "American Studies",
            "Anthropology",
            "Art",
            "Asian Studies",
            "Aviation Science",
            "Biochemistry",
            "Biology",
            "Canadian Studies",
            "Cape Verdean Studies",
            "Chemistry",
            "Childhood Studies",
            "Civic Education and Community Leadership",
            "Classical Studies",
            "Communication",
            "Communication Sciences and Disorders",
            "Computer Science",
            "Cybersecurity and Digital Forensics",
            "Criminal Justice",
            "Dance",
            "Early Childhood Education",
            "Economics",
            "English",
            "Environmental Science and Sustainability",
            "Exercise Physiology",
            "Film",
            "Geography",
            "Geological Sciences",
            "Global Languages and Literatures",
            "Global Religious Studies",
            "Health Science",
            "History",
            "Irish Studies",
            "Latin American and Caribbean Studies",
            "LGBTQ Studies",
            "Literacy Studies",
            "Management and Marketing",
            "Mathematics",
            "Middle East Studies",
            "Music",
            "Native American and Indigenous Studies",
            "Philosophy",
            "Physics",
            "Political Science",
            "Portuguese",
            "Pre-Law",
            "Psychology",
            "Public Health",
            "Public Relations",
            "Secondary Education",
            "Social Studies",
            "Social Work",
            "Sociology",
            "Spanish",
            "Special Education",
            "Sustainability",
            "Teaching English to Speakers of Other Languages (TESOL)",
            "Theatre",
            "Urban Studies",
            "Women's and Gender Studies"
        ]

        for dept in departments:
            obj, created = Department.objects.get_or_create(name=dept)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created department: {dept}"))
            else:
                self.stdout.write(f"Department already exists: {dept}")

        self.stdout.write(self.style.SUCCESS("Department population complete."))
