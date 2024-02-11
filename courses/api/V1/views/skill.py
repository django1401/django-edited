from ..serializer import SkillsSerializer
from ....models import Skills
from rest_framework import viewsets

class SkillsView(viewsets.ModelViewSet):
    serializer_class = SkillsSerializer
    queryset = Skills.objects.all()
