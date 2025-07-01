from django.db import models
from django.contrib.auth import get_user_model
CustomUser = get_user_model()
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    number_of_employees = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name


class CompanyEmployee(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='company_employee_profile')
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='company_employees')
    position = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Company Contact: {self.user.username} at {self.company.name} ({self.position or 'N/A'})"


class Skill(models.Model):
    name = models.CharField(
        max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Candidate(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='candidate_profile')
    resume = models.FileField(upload_to='static/resumes/')
    description = models.TextField()
    education = models.CharField(max_length=255, )
    years_of_experience = models.PositiveIntegerField()
    skills = models.ManyToManyField(Skill, related_name='skills')

    def __str__(self):
        return f"Candidate: {self.user.username} ({self.user.email})"


class Job(models.Model):
    employer_name = models.ForeignKey(
        CompanyEmployee, on_delete=models.CASCADE, related_name='jobs')
    context = models.TextField()
    appliers_count = models.PositiveSmallIntegerField()


class JobApplier(models.Model):
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name='appliers')
    applier = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, related_name='candidates')
