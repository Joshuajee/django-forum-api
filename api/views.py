from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Topic, Comments
from .serializers import TopicSerilizers, CommentsSerilizers, UserSerilizer
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .tokens import get_tokens_for_user
# Create your views here.

@api_view(["GET"])
def index(req):
    
    return Response({
        "status": "Success", 
        "message": "Hello, My first API"
    })
    
@api_view(["POST"])
def sign_up(req): 
    first_name  =  req.data["first_name"]
    last_name  =  req.data["last_name"]
    password  =  req.data["pass"]
    username  =  req.data["username"]
    email  =  req.data["email"]
    
    User.objects.create_user(
        first_name=first_name, last_name=last_name, 
        password=password, username=username,
        email=email
    )
    return Response({"message": "Account created"}, status=HTTP_201_CREATED)

@api_view(["POST"])
def login(req):
    password  =  req.data["pass"]
    username  =  req.data["username"]
    user  =  authenticate(req, username = username, password  = password)
    if user != None:
        token =  get_tokens_for_user(user)
        return Response(
            {   
                "access_token": token["access"],
                "refresh_token": token["refresh"],
                "message": "Login successfully"
            }, 
            status = HTTP_200_OK
        ) 
    else: 
        return Response({message: "Invalid username of Password"}, status = HTTP_401_UNAUTHORIZED) 
    
    return Response("")



@api_view(["GET"])
def topic(req):
    topics = Topic.objects.all()
    return Response(TopicSerilizers(topics, many=True).data)

@api_view(["GET"])
def get_topic(req, id):
    topics = Topic.objects.get(id=id)
    return Response(TopicSerilizers(topics).data)

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
@permission_classes([IsAuthenticated])
def create_topic_auth(req):
    author = req.user   
    print(author) 
    topic = TopicSerilizers(data=req.data)
    if topic.is_valid():
        topic.author = author.id
        topic.save()
        return Response({"message": "Topic created"}, status=HTTP_201_CREATED)
    else:
        return Response(topic.errors, status=HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(req):
    user = User.objects.get(username=req.user)
    return Response(UserSerilizer(user).data, status=HTTP_200_OK)
    

@api_view(["PATCH"])
def update_topic(req, id):
    topic = Topic.objects.get(id=id)
    topic.content = req.data['content']
    topic.save()
    return Response({"message": "Topic updated"}, status=HTTP_200_OK)


@api_view(["DELETE"])    
def delete_topic(req, id): 
    topic = Topic.objects.get(id=id)
    topic.delete()
    return Response({"message": "Deleted Successfully"})
    
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