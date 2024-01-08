from django.db import models

# Create your models here.

class User(models.Model):
   email=models.EmailField(unique=True, max_length=50)
   password=models.CharField(max_length=20)
   role=models.CharField(max_length=20)  # chairman/member
   isActive=models.BooleanField(default=False)
   created_at=models.DateTimeField(auto_now=True)
   
   def __str__(self):
       return f"{self.email} | {self.role}"
   
class Chairman(models.Model):
   userid=models.ForeignKey(User, on_delete=models.CASCADE)
   firstname = models.CharField(max_length = 20)
   lastname = models.CharField(max_length=20)
   contact = models.CharField(max_length=11)
   blockno = models.CharField(max_length=3)
   houseno = models.CharField(max_length=4)
   pic=models.FileField(upload_to='media/upload', default='default.png')

   def __str__(self):
       return f"{self.firstname} | {self.blockno}/{self.houseno}"
   
class Member(models.Model):
   userid=models.ForeignKey(User, on_delete=models.CASCADE)
   firstname = models.CharField(max_length = 20)
   lastname = models.CharField(max_length=20)
   contact = models.CharField(max_length=11)
   blockno = models.CharField(max_length=3)
   houseno = models.CharField(max_length=4)
