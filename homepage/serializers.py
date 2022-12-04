from rest_framework import serializers
from .models import *

class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = '__all__'
        lookup_field = 'slug'