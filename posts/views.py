from aiogram.fsm.context import FSMContext
from rest_framework import generics
from rest_framework.response import Response

from handlers.users.start import send_contact_info, send_order_info, send_order_info_full_phone, \
    send_contact_info_full_number
from .models import Project, Comment, Order, Project_Type, Tariff
from .serializers import (
    ProjectDetailSerializer,
    ProjectsSerializer,
    CommentSerializer,
    OrderSerializer,
    ProjectTypesSerializer
)

import asyncio
import concurrent.futures


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
            user_id = serializer.data.get('id')
            fullname = serializer.data.get('fullname')
            project_type_id = serializer.data.get('project_type')
            project_tariff_id = serializer.data.get('tariff')
            project_type = Project_Type.objects.get(pk=project_type_id)
            project_tariff = Tariff.objects.get(pk=project_tariff_id)
            message = serializer.data.get('message')
            phone = serializer.data.get('phone')

            if '+998' not in phone[0:4]:
                asyncio.run(
                    send_order_info(user_id, fullname, phone, project_type.title, project_tariff.title, message))
            elif '+998' in phone[0:4]:
                asyncio.run(
                    send_order_info_full_phone(user_id, fullname, phone, project_type.title, project_tariff.title,
                                               message))

            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class ProjectTypesListApiView(generics.ListAPIView):
    queryset = Project_Type.objects.all()
    serializer_class = ProjectTypesSerializer
