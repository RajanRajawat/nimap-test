from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer, ClientProjectSerializer, UserSerializer

# Create your views here.


class ClientListView(APIView):

    def get(self, *args):
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request):
        request.user = User.objects.get(username='rajan') #Need toUpdate Authentication tomorrow morning
        data = request.data
        client_name = data.get('client_name')
        client = Client.objects.create(client_name=client_name, created_by=request.user)
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ClientView(APIView):

    def get(self, request, client_id):
        client = Client.objects.get(pk=client_id)
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def patch(self, request, client_id):
        data = request.data
        client_name = data.get('client_name')
        client = Client.objects.get(pk=client_id)
        client.client_name = client_name
        client.save()
        client.refresh_from_db()
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, client_id):
        Client.objects.filter(pk=client_id).delete()
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)


class ClientProjectsView(APIView):

    def post(self, request, client_id):
        request.user = User.objects.get(username='rajan') #Authentication
        data = request.data
        project_name = data.get('project_name')
        users = data.get('users')
        user_ids = [user['id'] for user in users]
        # deserialized_users = UserSerializer(data=users, many=True)
        project = Project.objects.create(project_name=project_name, client_id=client_id, created_by=request.user)
        project.users.set(user_ids)
        serializer = ClientProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectView(APIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request):
        projects = Project.objects.filter()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    