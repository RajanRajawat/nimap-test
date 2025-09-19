from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.CharField(max_length=25) #This should be auto from logged in user
    created_by = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    
    def __str__(self):
        return self.client_name
    
class Project(models.Model):
    project_name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.CharField(max_length=25) #To be updated as well
    created_by = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.project_name



#Allowed to use default user model
