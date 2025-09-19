from django.urls import path, include
from .views import ClientView, ProjectView, ClientListView, ClientProjectsView


urlpatterns = [
    path('clients', (ClientListView.as_view())),
    path('clients/<int:client_id>', (ClientView.as_view())),
    path('clients/<int:client_id>/projects', (ClientProjectsView.as_view())),
    path('projects', (ProjectView.as_view())),
]