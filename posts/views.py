from aiogram.fsm.context import FSMContext
from rest_framework import generics
from rest_framework.response import Response

from .models import Project, Comment, Order, Project_Type, Tariff
from .serializers import (
    ProjectDetailSerializer,
    ProjectsSerializer,
    CommentSerializer,
    OrderSerializer,
    ProjectTypesSerializer
)




class ProjectsListApiView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer


class ProjectDetailApiView(generics.RetrieveAPIView):
    serializer_class = ProjectDetailSerializer
    queryset = Project.objects.all()


class CommentListApiView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class OrderCreateApiView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class ProjectTypesListApiView(generics.ListAPIView):
    queryset = Project_Type.objects.all()
    serializer_class = ProjectTypesSerializer
