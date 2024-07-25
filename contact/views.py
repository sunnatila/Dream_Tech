import asyncio

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from contact.models import Contact
from contact.serializers import ContactSerializer


class ContactCreateApiView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
