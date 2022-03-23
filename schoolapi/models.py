from django.db import models
from django.utils.translation import gettext_lazy as _
import os

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
        
class Subject(TimeStamp):
    subject_id = models.AutoField(primary_key=True, null=False)
    subject_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')
        
    def __str__(self) -> str:
        return self.subject_name

class Teacher(TimeStamp):
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

# To change the name of images with the title of the instance of the class
def name_of_image(instance, filename):
    if hasattr(instance, 'imgpath'):
        if os.path.exists(instance.imgpath):
            os.remove(instance.imgpath)
            
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (instance.title, ext)
    instance.title = blocks[0]
    instance.imgpath = os.path.join('manaslu/notice/', filename)
    return instance.imgpath
    
class Notice(TimeStamp):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to=name_of_image, blank=True, null=True)
    notice_date = models.DateField(blank=True, null=True)
    
    class Meta:
        verbose_name = _('Notice')
        verbose_name_plural = _('Notices')

    def __str__(self) -> str:
        return self.title
    
   
class Event(TimeStamp):
    title = models.CharField(max_length=100)
    description = models.TextField()
    organizer = models.CharField(max_length=100, null=True, blank=True)
    participants = models.CharField(max_length=100, null=True, blank=True)
    published_date = models.DateField()
    no_of_days = models.IntegerField(blank=True, default=1)
    event_date = models.DateField()

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self) -> str:
        return self.title