from rest_framework import serializers
from .models import Knihovna

class KnihovnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Knihovna
        fields = '__all__'