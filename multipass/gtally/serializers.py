from rest_framework import serializers
from .models import Tally

class TallySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tally
        fields = ('id','game','winner','w_score','l_score','date')