
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializer import CourseSerializer, CourseDetailSerializer
from ...models import Course
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin




# @api_view(["GET", "POST"])
# @permission_classes([IsAdminUser])
# def course_api_view(request):
#     if request.method == 'GET':
#         courses = Course.objects.filter(status=True)
#         courses_serilize = CourseSerializer(courses, many=True)
#         return Response(courses_serilize.data)
#     elif request.method == "POST":
#         course_serilize = CourseDetailSerializer(data=request.data)
#         if course_serilize.is_valid():
#             course_serilize.save()
#             return Response(course_serilize.data)
#         else:
#             return Response(course_serilize.errors)
        





# @api_view(["GET", "PUT", "DELETE"])
# def course_api_detail_view(request, pk):
#     course = get_object_or_404(Course, id=pk)
#     if request.method == "GET":
#         course_serilize = CourseDetailSerializer(course)
#         return Response(course_serilize.data)
#     elif request.method == "PUT":
#         course_serilize = CourseDetailSerializer(course, data=request.data)
#         course_serilize.is_valid(raise_exception=True)
#         course_serilize.save()
#         return Response(course_serilize.data)
#     elif request.method == "DELETE":
#         course.delete()
#         return Response("course deleted", status=status.HTTP_204_NO_CONTENT)




class CourseListView(APIView):
    #permission_classes = [IsAdminUser]
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        courses = Course.objects.filter(status=True)
        courses_serilize = CourseSerializer(courses, many=True)
        return Response(courses_serilize.data)
    def post(self, request, *args, **kwargs):
        course_serilize = CourseDetailSerializer(data=request.data)
        if course_serilize.is_valid():
            course_serilize.save()
            return Response(course_serilize.data)
        else:
            return Response(course_serilize.errors)
        

class CourseDetailView(APIView):
        
    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course, id=kwargs['pk'])
        course_serilize = CourseDetailSerializer(course)
        return Response(course_serilize.data)
    
    def put(self, request, *args, **kwargs):
        course = get_object_or_404(Course, id=kwargs['pk'])
        course_serilize = CourseDetailSerializer(course, data=request.data)
        course_serilize.is_valid(raise_exception=True)
        course_serilize.save()
        return Response(course_serilize.data)

    def delete(self, request, *args, **kwargs):
        course = get_object_or_404(Course, id=kwargs['pk'])
        course.delete()
        return Response("course deleted", status=status.HTTP_204_NO_CONTENT)


# class CourseDetailView(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    


#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)