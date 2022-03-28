from dataclasses import field
from rest_framework import serializers
from .models import Teacher, Subject, Event, Notice

#  -------------------Teacher Serializer ------------------ #

class TeacherCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = ["id", "full_name", "address", "email", "dob", "contact_number", "qualification", "skills", "hobbies", "joined_date", "salary", "subject"]


class TeacherListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = "__all__"
        


class TeacherUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = ["address", "email", "contact_number", "qualification", "skills", "salary"]

# --------------------- Events Serializer ------------------ #

class EventCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ["id", "title", "description", "organizer", "participants", "published_date", "no_of_days", "event_date"]

class EventListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = "__all__"
        


class EventUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ["title", "description", "organizer", "participants", "no_of_days", "event_date"]
        

# ------------------- Notice ----------------- #

class NoticeCreateSerialzier(serializers.ModelSerializer):
    
    class Meta:
        model = Notice
        fields = ["id", "title", "description", "photo", "notice_date", "published_date"]

class NoticeListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notice
        fields = "__all__"
        
class NoticeUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notice 
        fields = ["title", "description", "photo", "notice_date"]