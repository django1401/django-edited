from rest_framework.generics import GenericAPIView
from ..serializer import ProfileSerializer
from ....models import Profile
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class ProfileView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        serializer = self.serializer_class(profile)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, *args, **kwargs):
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        serializer = self.serializer_class(profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)