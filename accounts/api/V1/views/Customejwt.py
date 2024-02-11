from ..serializer import CustomObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class Customejwtview(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer