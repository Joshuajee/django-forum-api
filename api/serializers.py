from rest_framework import serializers
from .models import Topic, Comments
from django.contrib.auth.models import User

class TopicSerilizers(serializers.ModelSerializer):
    
    class Meta:
        model = Topic
        fields = ["id","author", "title", "content", "views"]
    
    
class CommentsSerilizers(serializers.ModelSerializer):
    
    class Meta:
        model = Comments
        fields = "__all__"
    
    
class UserSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email"]