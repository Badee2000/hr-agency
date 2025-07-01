from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AgencyEmployee
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin as DefaultGroupAdmin
from .models import AgencyEmployeeUser, CandidateUser, CompanyEmployeeUser, Position
from clients.models import Candidate, CompanyEmployee
from chats.models import AIChat, Chat

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class GroupAdmin(DefaultGroupAdmin):
    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    model = Position


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = (
        ('Registration', {
            'fields': ('username', 'email', 'first_name', 'last_name', 'phone', 'address', 'password1', 'password2'),
        }),
    )
    list_display = ['username', 'email', 'role',
                    'first_name', 'last_name', 'is_staff']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(pk=request.user.pk)

    # def has_change_permission(self, request, obj=None):
    #     if request.user.is_superuser:
    #         return True
    #     if obj is not None and obj == request.user:
    #         return True
    #     return False

    # def has_add_permission(self, request):
    #     return request.user.is_superuser

    # def has_delete_permission(self, request, obj=None):
    #     return request.user.is_superuser


# Inlines
class AgencyEmployeeInline(admin.StackedInline):
    model = AgencyEmployee
    fields = ('position',)
    can_delete = False
    verbose_name_plural = 'Agency Employee Fields'
    fk_name = 'user'
    max_num = 1
    min_num = 1


class CandidateInline(admin.StackedInline):
    model = Candidate
    fields = ('resume', 'description', 'education',
              'years_of_experience', 'skills',)
    can_delete = False
    verbose_name_plural = 'Candidate Fields'
    fk_name = 'user'
    max_num = 1
    min_num = 1


class CompanyEmployeeInline(admin.StackedInline):
    model = CompanyEmployee
    fields = ('company', 'position')
    can_delete = False
    verbose_name_plural = 'Company Employee Fields'
    fk_name = 'user'
    max_num = 1
    min_num = 1


# Proxies
@admin.register(AgencyEmployeeUser)
class AgencyEmployeeUserAdmin(CustomUserAdmin):
    role_value = 'agency_employee'
    inlines = [AgencyEmployeeInline]

    def save_model(self, request, obj, form, change):
        is_new = not obj.pk

        if not change and self.role_value:
            obj.role = self.role_value
        obj.is_staff = True
        super().save_model(request, obj, form, change)

        # if is_new:
        #     try:
        #         group = Group.objects.get(name='Agency Employees')
        #         obj.groups.add(group)
        #     except Group.DoesNotExist:
        #         pass

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(role=self.role_value)


# Candidate proxy
@admin.register(CandidateUser)
class CandidateUserAdmin(CustomUserAdmin):
    role_value = 'candidate'
    inlines = [CandidateInline]

    def save_model(self, request, obj, form, change):
        is_new = not obj.pk
        if not change and self.role_value:
            obj.role = self.role_value
        super().save_model(request, obj, form, change)
        # if is_new:
        #     try:
        #         group = Group.objects.get(name='Candidate')
        #         obj.groups.add(group)
        #     except Group.DoesNotExist:
        #         pass

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(role=self.role_value)


# Company Employee proxy
@admin.register(CompanyEmployeeUser)
class CompanyEmployeeUserAdmin(CustomUserAdmin):
    role_value = 'company_employee'
    inlines = [CompanyEmployeeInline]

    def save_model(self, request, obj, form, change):
        is_new = not obj.pk
        if not change and self.role_value:
            obj.role = self.role_value
        super().save_model(request, obj, form, change)

        # if is_new:
        #     try:
        #         group = Group.objects.get(name='Company Employee')
        #         obj.groups.add(group)
        #     except Group.DoesNotExist:
        #         pass

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(role=self.role_value)


admin.site.unregister(Group)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Group, GroupAdmin)
