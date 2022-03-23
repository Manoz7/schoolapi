from ast import Sub
from django.contrib import admin
from schoolapi.models import Teacher, Subject
# Register your models here.


admin.site.register((Teacher, Subject))