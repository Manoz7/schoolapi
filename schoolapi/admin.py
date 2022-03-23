from django.contrib import admin
from schoolapi.models import Teacher, Subject, Event, Notice
# Register your models here.


admin.site.register((Teacher, Subject, Event, Notice))