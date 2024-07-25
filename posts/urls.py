from .views import (
    ProjectDetailApiView,
    ProjectsListApiView,
    CommentListApiView,
    OrderCreateApiView,
    ProjectTypesListApiView,
)
from django.urls import path

urlpatterns = [
    path('posts/list/', ProjectsListApiView.as_view()),
    path('posts/detail/<int:pk>/', ProjectDetailApiView.as_view()),
    path('comments/list/', CommentListApiView.as_view()),

    path('order/create/', OrderCreateApiView.as_view()),
    path('project_type/list/', ProjectTypesListApiView.as_view()),
]

