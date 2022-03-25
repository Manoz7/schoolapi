from django.urls import path
from schoolapi.views import *

urlpatterns = [

# --------------------- Teacher URLS ----------------- #
path("teacher/", TeacherListAPIView.as_view(), name="teacherlistapi"),
path("teacher/create", TeacherCreateAPIView.as_view(), name="teachercreateapi"),
path("teacher/detail/<slug:slug>/", TeacherDetailAPIView.as_view(), name="teacherdetailapi"),
path("teacher/update/<slug:slug>/", TeacherUpdateAPIView.as_view(), name="teacherupdateapi"),
path("teacher/delete/<slug:slug>/", TeacherDeleteAPIView.as_view(), name="teacherdeleteapi"),


# --------------------- Events URLS ----------------- #
path("event/", EventListAPIView.as_view(), name="eventlistapi"),
path("event/create", EventCreateAPIView.as_view(), name="eventcreateapi"),
path("event/detail/<int:pk>/", EventDetailAPIView.as_view(), name="eventdetailapi"),
path("event/update/<int:pk>/", EventUpdateAPIView.as_view(), name="eventupdateapi"),
path("event/delete/<int:pk>/", EventDeleteAPIView.as_view(), name="eventdeleteapi"),

# --------------------- Notices URLS ----------------- #
path("notice/", NoticeListAPIView.as_view(), name="noticelistapi"),
path("notice/create", NoticeCreateAPIView.as_view(), name="noticecreateapi"),
path("notice/detail/<int:pk>/", NoticeDetailAPIView.as_view(), name="noticedetailapi"),
path("notice/update/<int:pk>/", NoticeUpdateAPIView.as_view(), name="noticeupdateapi"),
path("notice/delete/<int:pk>/", NoticeDeleteAPIView.as_view(), name="noticedeleteapi"),



]