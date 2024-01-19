from django.shortcuts import render

# Create your views here.
def home(request):
   return render(request, "myapp/index.html")

def userForm(request):
   return render(request, 'myapp/userForm.html')