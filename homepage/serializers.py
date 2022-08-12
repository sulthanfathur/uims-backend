from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = '__all__'
        lookup_field = 'slug'

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'
        depth = 1