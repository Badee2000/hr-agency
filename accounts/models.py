from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    USER_ROLES = (
        ('agency_employee', 'Agency Employee'),
        ('candidate', 'Candidate'),
        ('company_employee', 'Company Employee'),
    )

    email = models.EmailField(unique=True, max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=50, choices=USER_ROLES,
                            blank=False, null=False, default='agency_employee')

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone']

    def __str__(self):
        return self.username

    @property
    def is_agency_employee(self):
        return self.role == 'agency_employee'

    @property
    def is_candidate(self):
        return self.role == 'candidate'

    @property
    def is_company_employee(self):
        return self.role == 'company_employee'


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AgencyEmployee(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='agency_employee_profile')
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.position}"


# Proxies

class AgencyEmployeeUser(CustomUser):
    class Meta:
        proxy = True
        verbose_name = "Agency Employee"
        verbose_name_plural = "Agency Employees"


class CandidateUser(CustomUser):
    class Meta:
        proxy = True
        verbose_name = "Candidate User"
        verbose_name_plural = "Candidate Users"


class CompanyEmployeeUser(CustomUser):
    class Meta:
        proxy = True
        verbose_name = "Candidate User"
        verbose_name_plural = "Company Employee Users"
