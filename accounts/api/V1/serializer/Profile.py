from ....models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
     email = serializers.CharField(max_length=100, source='user.email', read_only=True)
     
     class Meta:
          model = Profile
          fields = ['id', 'first_name', 'last_name', 'image', 'email']