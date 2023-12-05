from rest_framework import serializers
from ...models import *


# class CourseApiSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=200)
#     price = serializers.IntegerField()


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ["id", "title", "price", "content", "category", "teacher", "image"]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]

class SkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = ["id", "name"]