from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Entry
from .serializers import EntrySerializer
from rest_framework import generics

# Create your views here.


class DSListCreate(generics.ListCreateAPIView):
    queryset = Dataset.objects.all()
    serializer_class = EntrySerializer


def personal_view(request):
    return render(request, "index_personal.html")