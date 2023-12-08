from rest_framework import serializers
from ...models import *
from accounts.models import CustomeUser, Profile


# class CourseApiSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=200)
#     price = serializers.IntegerField()


class CourseSerializer(serializers.ModelSerializer):
    #content = serializers.ReadOnlyField()
    #content = serializers.CharField(read_only=True)
    price = serializers.SerializerMethodField()
    detail_link = serializers.SerializerMethodField(method_name='detail')

    class Meta:
        model = Course
        fields = ["id", "title", "price", "content", "category", "teacher", "image", 'detail_link']
        read_only_fields = ["content"]

    def get_price(self,obj):
        return obj.price * 50000
    
    def detail(self,obj):
        pass


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]

class SkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = ["id", "name"]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomeUser
        fields = ["id", "email"]