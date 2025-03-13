
from django.contrib import admin
from .models import Department, Subject, Roadmap, Professor

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'credit_hours')
    search_fields = ('name', 'department__name')

class RoadmapAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    filter_horizontal = ('semester1', 'semester2', 'semester3', 'semester4',
                         'semester5', 'semester6', 'semester7', 'semester8')

admin.site.register(Department)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Roadmap, RoadmapAdmin)
admin.site.register(Professor)
