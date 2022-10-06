from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Coordinator(models.Model):
    coordinator = models.OneToOneField(User,null= True, on_delete = models.CASCADE)
    name = models.CharField(max_length= 100 ,null= True)
    def __str__(self):
		    return self.name
