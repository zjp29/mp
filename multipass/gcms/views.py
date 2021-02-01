from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Dataset, URLs
from .serializers import DSSerializer
from rest_framework import generics

# Create your views here.

# class HomeView(View):
#     def get(self,request,*args,**kwargs):
#         return render(request,"index.html",{})
    

class DSListCreate(generics.ListCreateAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DSSerializer