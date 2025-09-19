from django.shortcuts import render
from .models import Client, Project
from django.contrib.auth.models import User
from .serializers import ClientSerializer, ProjectSerializer, UserSerializer, ClientProjectSerializer
from rest_framework import viewsets

# Create your views here.

class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    