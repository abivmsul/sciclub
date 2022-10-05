from django.db import models

# Create your models here.

class Student(models.Model): 
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    grade = models.CharField(max_length=20)
    accepted = models.BooleanField(default=False)
    department = models.CharField(max_length=50)
    idea = models.TextField()
       
    def __str__(self):
         return f"{self.fname} of grade {self.grade}"