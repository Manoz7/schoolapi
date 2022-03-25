from django.http import Http404
from django.shortcuts import render
from .serializers import EventCreateSerializer, EventListSerializer, EventUpdateSerializer, NoticeListSerializer, TeacherCreateSerializer, TeacherListSerializer, TeacherUpdateSerializer, NoticeCreateSerialzier, NoticeUpdateSerializer
from .models import Teacher, Event, Notice, Subject
from rest_framework.views import APIView

from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema



# -------------------Teacher API View -------------------- #
class TeacherCreateAPIView(APIView):
    
    @swagger_auto_schema(request_body=TeacherCreateSerializer)
    def post(self, request):
        """
            Create a teacher instance
        """
        serializer = TeacherCreateSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
            resp = {
                "status": "success",
                "message": "Teacher is created!",
                "data": serializer.data
            }
            
            return Response(resp)
        
        else:
            resp = {
                "status": "failure",
                "message": serializer.errors
            }
            return Response(resp)
    


class TeacherListAPIView(APIView):
    
    """
        List all teachers
    """
    
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherListSerializer(teachers, many=True)
        return Response(serializer.data)
    


class TeacherDetailAPIView(APIView):
    """
        Retrieve a teacher instance
    """
    
    def get_object(self, slug):
        try:
            return Teacher.objects.get(slug=slug)
        
        except Teacher.DoesNotExist:
            return Http404
    
    def get(self, request, slug):
        teacher = self.get_object(slug=slug)
        serializer = TeacherListSerializer(teacher)
        return Response(serializer.data)
    

class TeacherUpdateAPIView(APIView):
    """
        Update a teacher instance
    """
    
    @swagger_auto_schema(request_body=TeacherUpdateSerializer)
    def patch(self, request, *args, **kwargs):
        slug_field = self.kwargs.get("slug")
        teacher = Teacher.objects.get(slug=slug_field)

        serializer = TeacherUpdateSerializer(teacher, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            resp = {
                "status": "success",
                "message": "Teacher instance is updated."
            }
            return Response(resp)

        else:
            resp = {
                "status": "failure",
                "message": serializer.errors
            }
            return Response(resp)

class TeacherDeleteAPIView(APIView):
    
    def delete(self, request, *args, **kwargs):
        slug_field = self.kwargs.get("slug")
        teacher_obj = Teacher.objects.get(slug=slug_field)
        
        teacher_obj.delete()
        resp = {
            "status": "success",
            "message": "Teacher instance is deleted."
        }
        return Response(resp)
    
    
# -------------------- Events -------------- #
class EventCreateAPIView(APIView):
    
    @swagger_auto_schema(request_body=EventCreateSerializer)
    def post(self, request):
        """
            Create a new event
        """
        serializer = EventCreateSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            resp = {
                "status": "success",
                "message": "Event is Created",
                "data": serializer.data
            }
            
            return Response(resp)
        
        else:
            resp = {
                "status": "failure",
                "message": serializer.errors
            }
            
            return Response(resp)
    

class EventListAPIView(APIView):
    """
        List all teachers
    """
    
    def get(self, request):
        teachers = Event.objects.all()
        serializer = EventListSerializer(teachers, many=True)
        return Response(serializer.data)

class EventUpdateAPIView(APIView):
    
    @swagger_auto_schema(request_body=EventUpdateSerializer)
    def patch(self, request, *args, **kwargs):
        """
            Update the event detail partially or fully
        """ 
        
        event_id = self.kwargs.get("pk")
        event_obj = Event.objects.get(id = event_id)
        
        try:          

            event_obj = Event.objects.get(id = event_id)
            serializer = EventUpdateSerializer(event_obj, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                resp = {
                    "status": "success",
                    "message": "An event is Updated",
                    "data": serializer.data
                }
                return Response(resp)
            else:
                resp = {
                    "status": "failure",
                    "message": serializer.errors
                }
                return Response(resp)
        
        except:
            resp = {
                "status": "failure",
                "message": "Item you want to update doesnot exist in database."
            }
            return Response(resp)

class EventDetailAPIView(APIView):
    """
        Retrieve an event instance
    """
    
    def get_object(self, request, pk):
        
        try:
            return Event.objects.get(pk=pk)
        
        except Event.DoesNotExist:
            return Http404
        
    
    def get(self, request, pk):
        """
            Get an event instance using id
        """
        event = self.get_object(pk)
        serializer = EventListSerializer(event)
        return Response(serializer.data)

class EventDeleteAPIView(APIView):
    
    def delete(self, request, *args, **kwargs):
        """
            Delete an event instance
        """
        
        pk = self.kwargs.get('pk')
        try:
            
            event_obj = Event.objects.get(id=pk)
            event_obj.delete()
            
            resp = {
                        "status": "success",
                        "message": "An event is deleted!"
                    }
                    
            return Response(resp)
        
        except:
            resp ={
                "status": "failure",
                "message": "Item you want to delete is already Deleted or doesn't existed."
            }
            return Response(resp)
    
    
    

# ------------------ Notice ----------------- #

class NoticeCreateAPIView(APIView):
    
    @swagger_auto_schema(request_body=NoticeCreateSerialzier)
    def post(self, request):
        """
            Create a notice instance 
        """
        serializer = NoticeCreateSerialzier(data = request.data)

        if serializer.is_valid():
            serializer.save()
            
            resp ={
                "status": "success",
                "message": "A notice is created!",
                "data": serializer.data
            }
            return Response(resp)
        
        else:
            resp = {
                "status": "failure",
                "message": serializer.errors
            }

class NoticeListAPIView(APIView):
    
    def get(self, request):
        """
            Get all notices
        """
        notices = Notice.objects.all()
        serializer = NoticeListSerializer(notices, many=True)
        return Response(serializer.data)


class NoticeDetailAPIView(APIView):
    
    def get_object(self, request, pk):
        
        try:
            return Notice.objects.get(pk=pk)
    
        except Notice.DoesNotExist:
            return Http404
    
    def get(self, request, pk):
        
        """
            Get a notice instance
        """
        notice = self.get_object(pk)
        serializer = NoticeListSerializer(notice)
        return Response(serializer.data)
        
    

class NoticeUpdateAPIView(APIView):
    
    @swagger_auto_schema(request_body=NoticeUpdateSerializer)
    def patch(self, request, *args, **kwargs):
        """
            Update the notice
        """
        pk = self.kwargs.get('pk')
        notice_obj = Notice.objects.get(id=pk)
        
        
        try: 
            notice_obj = Notice.objects.get(id=pk)
            serializer = NoticeUpdateSerializer(notice_obj, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                resp = {
                    "status": "success",
                    "message": "Notice instance is Updated",
                    "data": serializer.data
                }
                return Response(resp)
            
            else:
                resp = {
                    "status": "failure",
                    "message": serializer.errors
                }
                return Response(resp)
            
            
        except:
            resp ={
                "status": "failure",
                "message": "Item you want to update doesn't exist."
            }
            return Response(resp)

class NoticeDeleteAPIView(APIView):
    
    def delete(self, request, *args, **kwargs):
        """
            Delete notice instance
        """
        
        pk = self.kwargs.get('pk')
        try:
            
            notice_obj = Notice.objects.get(id=pk)
            notice_obj.delete()
            
            resp = {
                        "status": "success",
                        "message": "A notice is deleted!"
                    }
                    
            return Response(resp)
        
        except:
            resp ={
                "status": "failure",
                "message": "Item you want to delete is already Deleted or doesn't existed."
            }
            return Response(resp)


