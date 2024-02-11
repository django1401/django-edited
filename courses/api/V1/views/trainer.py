from ..serializer import TrainerSerializer
from ....models import Trainer 
from rest_framework import viewsets


class TrainerView(viewsets.ModelViewSet):
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.filter(status=True)