# HONORS PROJECT
## Bridgewater State University Academic Roadmap

### Student: Natalio Gomes
### Mentor: Dr. Nolin
### Class: COMP 335 -  WEB DEVELOPMENT

A comprehensive Django-based application designed to help Bridgewater State University students explore and navigate curriculum pathways based on their intended career goals.

## Project Overview

The BSU Academic Roadmap serves as a central resource for students to plan their academic journey. Unlike traditional course catalogs, this system emphasizes career outcomes by showing how different course combinations can lead to different professional settings. For example, two computer science students might follow different roadmaps depending on whether they're interested in software development, data science, cybersecurity, or other specialized fields.

## Key Features

### For Students (Public Frontend)
- Browse departments, subjects, professors, and roadmaps without login requirements
- Filter subjects and roadmaps by department
- View detailed semester-by-semester curriculum plans
- See credit hour calculations for each year and program total
- Discover which professors teach specific subjects
- Explore alternate roadmaps within the same department
- Understand how specific subjects fit into various roadmaps

### For Administrators (Secure Backend)
- Secure login for administrative personnel
- Comprehensive dashboard for content management
- Create, view, update, and delete departments, subjects, professors, and roadmaps
- Upload visual representations of roadmap paths
- Manage professor profiles with photos
- Build semester-by-semester curriculum roadmaps

## System Architecture

### Models
- **Department**: Academic departments within the university
- **Subject**: Individual courses with credit hours and descriptions
- **Professor**: Faculty information including profile photos and associated subjects
- **Roadmap**: Semester-by-semester curriculum plans (8 semesters) with credit calculations

### Components
- **Public Frontend**: Accessible to all students without login
- **Administrative Backend**: Secure interface for authorized personnel
- **Dashboard**: Central management console
- **Pagination**: For handling large datasets of subjects
- **Filtering**: Department-based filtering for subjects and roadmaps

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Configure database settings in `settings.py`
5. Run migrations:
   ```
   python manage.py migrate
   ```
6. Create a superuser for administrative access:
   ```
   python manage.py createsuperuser
   ```
7. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

### For Students
1. Navigate to the homepage to see featured departments, roadmaps, subjects, and professors
2. Browse all departments or view a specific department's offerings
3. Explore subject listings with department filtering
4. View detailed roadmaps with semester breakdowns and credit calculations
5. Learn about professors and their teaching areas

### For Administrators
1. Access the secure login page
2. Navigate the dashboard to manage all content
3. Add/edit departments, subjects, professors, and roadmaps
4. Create comprehensive roadmaps by assigning subjects to specific semesters
5. Track relationships between subjects, professors, and roadmaps

## Project Structure

```
BSU-AR/
├── BackEnd/                 # Administrative application
│   ├── models.py            # Database models
│   ├── forms.py             # Forms for data input
│   ├── views.py             # Administrative view controllers
│   └── templates/           # Admin interface templates
├── FrontEnd/                # Public-facing application
│   ├── views.py             # Public view controllers
│   └── templates/           # Public interface templates
│       ├── index.html       # Homepage template
│       └── frontend/        # Section-specific templates
├── media/                   # User-uploaded files (professor photos, roadmap images)
├── static/                  # CSS, JavaScript, and static assets
└── manage.py                # Django management script
```

## Features in Detail

### Homepage
- Featured departments
- Showcase of recent roadmaps
- Highlighted subjects
- Featured professors

### Subject Management
- Department association
- Credit hour tracking
- Professor associations
- Roadmap placement tracking

### Roadmap Builder
- Department-specific roadmaps
- Semester-by-semester planning
- Credit hour calculations by year and total
- Visual representations with uploaded posters

### Professor Directory
- Profile management with photos
- Subject associations
- Department affiliations

## Development Guidelines

- Follow Django's best practices for view organization
- Maintain separation between public and administrative interfaces
- Implement proper filtering and pagination for better user experience
- Ensure mobile responsiveness for student access across devices

## Future Enhancements

- Student accounts with personal roadmap tracking
- Progress monitoring against chosen roadmaps
- Prerequisite visualization and enforcement
- Integration with university registration systems
- Career outcome statistics and alumni testimonials

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request with a clear description of improvements



## Contact

Natalio Gomes
www.nataliogomes.tech
