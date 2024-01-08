from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
   return render(request, "myapp/login.html")

# def login(request):
#    if request.POST:
#       try:
#          user_email=request.POST['email']
#          user_password=request.POST['password']
#          print("=========>>>",user_email,user_password)
         
#          user_data=User.objects.get(email=user_email, password=user_password)
#          print("=========>>>",user_data)
         
#          return render(request, "myapp/login.html")
#       except Exception as e:
#          print("===========>>> Error =",e)
#          msg="Invalid Input Pls Enter Again"
#          return render(request, "myapp/login.html", {'msg':msg})
         
#    else:
#       print("=========>>> Login")
#       return render(request, "myapp/login.html")

def login(request):
   if 'email' in request.session:
      return render(request, 'myapp/index.html')
   else:
      msg=False
      try:
         # user input
         print("=========>>> Login")
         user_email=request.POST.get('email')
         user_password=request.POST.get('password')
         print("=========>>>",user_email,user_password)
         
         if(user_email != None and user_password != None):
            # user object/row
            user_data=User.objects.get(email=user_email, password=user_password)
            chairman_data=Chairman.objects.get(userid=user_data.id)
            print("=========>>>",user_data,chairman_data)
            
            request.session['email']=user_data.email
            
            return render(request, 'myapp/index.html')
         
      except Exception as e:
         print("===========>>> Error =",e)
         msg="Invalid Input Pls Enter Again"
         
         
      return render(request, "myapp/login.html", {'msg':msg})
