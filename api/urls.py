from django.urls import path, include
from .views import index, topic, comments, create_topic

urlpatterns = [
    path("hello", index),
    path("topics", topic),
    path("comments/<id>", comments),
    path("create-topic", create_topic)
]
