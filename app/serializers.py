from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User


class ClientS(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.username")
    class Meta:
        model = Client
        fields=['id', 'client_name', 'created_at', 'created_by', ]

class ProjectS(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields=['id', 'project_name', 'created_at', 'created_by']
        
class UserS(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']