from rest_framework import serializers
from .models import Topic, Comments

class TopicSerilizers(serializers.ModelSerializer):
    
    class Meta:
        model = Topic
        fields = ["author", "title", "content", "views"]
    
    
class CommentsSerilizers(serializers.ModelSerializer):
    
    class Meta:
        model = Comments
        fields = "__all__"
    