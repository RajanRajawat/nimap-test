from django.urls import path, include
from .views import ClientView, ProjectView, ClientListView, ClientProjectsView


urlpatterns = [
    # GET // POST
    
    path('clients/', (ClientListView.as_view())),
    # GET // PATCH // DELETE
    path('clients/<int:client_id>/', (ClientView.as_view())),
    # POST
    path('clients/<int:client_id>/projects/', (ClientProjectsView.as_view())),
    # GET
    path('projects', (ProjectView.as_view())), 
]