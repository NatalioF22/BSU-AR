from django.core.management.base import BaseCommand
from BackEnd.models import Subject
import csv

class Command(BaseCommand):
    help = 'Import courses from CSV file into the database.'
    
    def handle(self, *args, **options):
        csv_file_path = 'BackEnd/management/commands/Extracted_Unique_Courses.csv'  # Path to your CSV file
        
        try:
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                
                # Counter for statistics
                created_count = 0
                existing_count = 0
                
                for row in csv_reader:
                    class_name = row['class_name']
                    title = row['title']
                    
                    # Check if the subject already exists by class_name
                    existing_subject = Subject.objects.filter(name=class_name).first()
                    
                    if existing_subject:
                        self.stdout.write(self.style.WARNING(f"Subject already exists: {class_name} - {title}"))
                        existing_count += 1
                    else:
                        # Create new subject with default credit hours = 3
                        subject = Subject.objects.create(
                            name=class_name,
                            title=title,
                            description=None,
                            credit_hours=3
                        )
                        self.stdout.write(self.style.SUCCESS(f"Created subject: {class_name} - {title}"))
                        created_count += 1
                
                self.stdout.write(self.style.SUCCESS(f"Import complete. Created {created_count} new courses, {existing_count} already existed."))
                
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"CSV file not found: {csv_file_path}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error importing courses: {str(e)}"))