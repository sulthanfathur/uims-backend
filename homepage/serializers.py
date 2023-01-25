from rest_framework import serializers
from .models import *

class HomepageBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomepageBanner
        fields = '__all__'

class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = '__all__'
        lookup_field = 'slug'