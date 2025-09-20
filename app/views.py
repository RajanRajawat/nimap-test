from django.contrib.auth.models import User
from rest_framework import status, authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer, ClientProjectSerializer, UserSerializer

# Create your views here.

# /clients
class ClientListView(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, *args):
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request):
        # request.user = User.objects.get(username='rajan') 
        created_by_user = request.user
        data = request.data
        client_name = data.get('client_name')
        client = Client.objects.create(client_name=client_name, created_by=created_by_user)
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# /clients/1
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

#/clients/1/projects
#Error
class ClientProjectsView(APIView):

    def post(self, request, client_id):
        # request.user = User.objects.get(username='rajan') #Authentication
        created_by_user = request.user
        data = request.data
        project_name = data.get('project_name')
        users = data.get('users')
        user_ids = [user['id'] for user in users]
        # deserialized_users = UserSerializer(data=users, many=True)
        project = Project.objects.create(project_name=project_name, client_id=client_id, created_by=created_by_user)
        project.users.set(user_ids)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

# /projects
class ProjectView(APIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request):
        projects = Project.objects.filter(users__id=request.user.id)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    