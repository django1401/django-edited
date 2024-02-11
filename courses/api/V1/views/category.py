from rest_framework.permissions import IsAuthenticated
from ..serializer import CategorySerializer
from ....models import Category 
from rest_framework import viewsets

class CategoryView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()