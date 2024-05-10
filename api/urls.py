from django.urls import path, include
from .views import sign_up, get_user, create_topic_auth, login, topic, comments, get_topic, create_topic, update_topic, delete_topic, create_comment

urlpatterns = [
    path("topics", topic),
    path("get-topic/<id>", get_topic),
    path("update-topic/<id>", update_topic),
    path("delete-topic/<id>", delete_topic),
    path("comments/<id>", comments),
    path("create-topic", create_topic),
    path("auth-create-topic", create_topic_auth),
    path("create-comment", create_comment),
    path("create-account", sign_up),
    path("login", login),
    path("get-user", get_user)
]
