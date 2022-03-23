
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True, null=False)
    subject_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')
        
    def __str__(self) -> str:
        return self.subject_name

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    dob = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    skills = models.CharField(max_length=100, null=True, blank=True)
    hobbies = models.CharField(max_length=200, null=True, blank=True)
    joined_date = models.DateField(blank=True, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')

    def __str__(self) -> str:
        return self.full_name
