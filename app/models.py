from django.db import models

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=25) #This should be auto from logged in user
    
    def __str__(self):
        return self.client_name
class Project(models.Model):
    pass

#Allowed to use default user
