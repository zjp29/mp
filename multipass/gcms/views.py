from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Dataset, URLs
from .serializers import DSSerializer
from rest_framework import generics

# Create your views here.


class DSListCreate(generics.ListCreateAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DSSerializer


# from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from rest_auth.registration.views import SocialLoginView
# class FacebookLogin(SocialLoginView):
#     adapter_class = FacebookOAuth2Adapter
# class GoogleLogin(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter