from django.urls import path, include
from .views import *


app_name = 'api-v1'

urlpatterns = [
    path("courses/",CourseListView.as_view(),name='courses'),
    path("course-detail/<int:pk>/",CourseDetailView.as_view(),name='course-detail'),

]
