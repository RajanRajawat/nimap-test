from django.urls import path, include
from .views import ClientView, ProjectView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clients', ClientView, basename='client')
router.register(r'projects', ProjectView, basename='project')

urlpatterns = [
    path('', include(router.urls) )
]