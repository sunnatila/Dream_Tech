import asyncio

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from contact.models import Contact
from contact.serializers import ContactSerializer
from handlers.users.start import send_contact_info, send_contact_info_full_number


class ContactCreateApiView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            fullname = serializer.data.get('fullname')
            phone = serializer.data.get('phone')
            message = serializer.data.get('message')
            user_id = serializer.data.get('id')

            if '+998' not in phone[0:4]:
                asyncio.run(send_contact_info(user_id, fullname, phone, message))
            elif '+998' in phone[0:4]:
                asyncio.run(send_contact_info_full_number(user_id, fullname, phone, message))
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
