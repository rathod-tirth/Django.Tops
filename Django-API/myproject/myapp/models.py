from django.db import models

# Create your models here.

class User(models.Model):
   name=models.CharField(max_length=30)
   age=models.CharField(max_length=50)   
   phone=models.CharField(max_length=10)
   city=models.CharField(max_length=20)
   state=models.CharField(max_length=20)
   
   def __str__(self):
       return self.name