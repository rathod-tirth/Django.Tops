from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

# Create your views here.

class GetUser(generics.ListCreateAPIView):
   queryset=User.objects.all()
   serializer_class=UserSerializer
   
class ControlUser(generics.RetrieveUpdateDestroyAPIView):
   queryset=User
   serializer_class=UserSerializer