from rest_framework import generics 
from gtally.serializers import TallySerializer
from gtally.models import Tally
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class TallyList(generics.ListAPIView):
    queryset = Tally.objects.all()
    serializer_class = TallySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id','winner','game')
    # search_fields = ('winner')

class TallyCreate(generics.CreateAPIView):
    serializer_class = TallySerializer