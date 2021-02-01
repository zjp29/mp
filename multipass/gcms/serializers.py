from rest_framework import serializers
from .models import Dataset, URLs

class DSSerializer(serializers.ModelSerializer):

    urls = serializers.PrimaryKeyRelatedField(many=True, queryset=URLs.objects.all())

    class Meta:
        model = Dataset
        fields = ('title','renewal','summary','detail','tags','f','urls')