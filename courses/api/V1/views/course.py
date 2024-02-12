from ..serializer import CourseSerializer
from ....models import Course
from rest_framework import viewsets
from .permission import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginator import CustomePaginate


class CourseView(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    serializer_class = CourseSerializer
    queryset = Course.objects.filter(status=True)
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ['category', 'title']
    search_fields = ['content', 'category__name', 'teacher__info__email']
    ordering_fields = ['created_date']
    pagination_class = CustomePaginate