from django.contrib import admin

from .models import Project, Report, User

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_per_page = 10

admin.site.register(Project, ProjectAdmin)

class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'project', 'date')
    list_display_links = ('id', 'user')
    search_fields = ('id', 'user', 'project')
    list_per_page = 10

admin.site.register(Report, ReportAdmin)

