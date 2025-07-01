# clients/admin.py
from django.contrib import admin
from .models import CompanyEmployee, Candidate, Company, Skill, Job, JobApplier
# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ['name', 'industry',
                    'number_of_employees', 'website', 'description']
    search_fields = ['name', 'industry']
    list_filter = ('industry',)



@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    model = Skill


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    model = Candidate


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    model = Job
    fields = ['context']

    def has_add_permission(self, request):
        if request.user.is_superuser or request.user.role == 'company_employee':
            return super().has_add_permission(request)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.employer_name = request.user
            obj.appliers_count = 0
            return super().save_model(request, obj, form, change)


@admin.register(JobApplier)
class JobApplierAdmin(admin.ModelAdmin):
    model = JobApplier
