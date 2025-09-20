from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User


class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.username")
    #need to add projects and updated tom morning
    # projects = serializers.StringRelatedField(many=True) #12
    class Meta:
        model = Client
        fields=['id', 'client_name', 'created_at', 'created_by', "updated_at" ] #-1-2
        read_only_fields = ["created_by"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        read_only_fields = ["username"]

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    created_by = serializers.CharField(source="created_by.username")
    client = serializers.CharField(source="client.client_name", read_only=True)

    class Meta:
        model = Project
        fields=['id', 'project_name', 'created_at', 'created_by', 'client', 'users']
        read_only_fields = ["created_by", 'client']


class ClientProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.username")
    projects = serializers.StringRelatedField(many=True)
    class Meta:
        model = Client
        fields=['id', 'client_name', 'created_at', 'created_by', 'projects' ]
        

class ClientListSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.username")
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by',]

        
        