from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Topic, Comments
from .serializers import TopicSerilizers, CommentsSerilizers
from rest_framework.status import *
# Create your views here.

@api_view(["GET"])
def index(req):
    
    return Response({
        "status": "Success", 
        "message": "Hello, My first API"
    })


@api_view(["GET"])
def topic(req):
    topics = Topic.objects.all()
    return Response(TopicSerilizers(topics, many=True).data)

@api_view(["GET"])
def comments(req, id):
    comments = Comments.objects.filter(topic=id)
    return Response(CommentsSerilizers(comments, many=True).data)


@api_view(["POST"])
def create_topic(req):
    author = req.user    
    topic = TopicSerilizers(data=req.data)
    if topic.is_valid():
        topic.author = author
        topic.save()
        return Response({"message": "Topic created"}, status=HTTP_201_CREATED)
    else:
        return Response(topic.errors, status=HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
def create_comment(req):
    author = req.user    
    comment = CommentsSerilizers(data=req.data)
    if comment.is_valid():
        comment.author = author
        comment.save()
        return Response({"message": "Comment created"}, status=HTTP_201_CREATED)
    else:
        return Response(comment.errors, status=HTTP_400_BAD_REQUEST)