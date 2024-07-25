from django.urls import path

from contact.views import ContactCreateApiView

urlpatterns = [
    path('contact/create/', ContactCreateApiView.as_view()),
]

