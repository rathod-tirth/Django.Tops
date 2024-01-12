from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.

def home(request):
   if 'email' in request.session:
      context=data(request.session['email'])   
      return render(request, 'myapp/index.html',context)
   
   return render(request, "myapp/login.html")

def login(request):
   if 'email' in request.session:
      context=data(request.session['email'])   
      return render(request, 'myapp/index.html',context)
   else:
      msg=False
      try:
         # getting user input from html
         print("=========>>> Login")
         user_email=request.POST.get('email')
         user_password=request.POST.get('password')
         print("=========>>>",user_email,user_password)
         
         if(user_email != None and user_password != None):
            # if the user input is correct get the user data as an object
            user_data=User.objects.get(email=user_email, password=user_password)
            chairman_data=Chairman.objects.get(userid=user_data.id)
            print("==============>>>",user_data,chairman_data)
            context={
                     "user":user_data,
                     "chairman":chairman_data,
                  }
            
            request.session['email']=context['user'].email
            
            print("========== render index")
            return render(request, 'myapp/index.html',context)
         
      except Exception as e:
         print("===========>>> Error =",e)
         msg="Invalid Input Pls Enter Again"
         
         
      return render(request, "myapp/login.html", {'msg':msg})
   
def logout(request):
   print("==============>>> logout")
   if "email" in request.session:
      del request.session['email']
   
   return render(request, "myapp/login.html")

# function for fetching user data
def data(f_email,f_password=None):
   user_data=User.objects.get(email=f_email)
   if f_password:
      user_data=User.objects.get(email=f_email, password=f_password)
      
   chairman_data=Chairman.objects.get(userid=user_data.id)
   print("==============>>>",user_data,chairman_data)
   context={
            "user":user_data,
            "chairman":chairman_data,
         }
   
   return context

def profile(request):
   context=None
   if 'email' in request.session:
      context=data(request.session['email'])
      
      if request.POST.get("c_password")!="" and request.POST.get("c_password")!=None:
         change_pass(request)
   else:
      return HttpResponseRedirect(reverse('login'))
   return render(request, 'myapp/profile.html', context)

def change_pass(request):
   c_password=request.POST.get("c_password")
   n_password=request.POST.get("n_password")
   print("===============>>> ",c_password,n_password)
   
   user=User.objects.get(email=request.session['email'])
   print("=========>>>> passsword :",user.password)
   
   if n_password!="" and n_password!=None:
      print("================>>>> Password checking")
      if user.password==c_password:
         user.password=n_password
         user.save()
         
         msg="Password Updated Successfully"
         return render(request, 'myapp/profile.html', {'msg':msg})
      else:
         print("================>>>> logging out")
         del request.session['email']
         return render(request, "myapp/login.html")
      
   return HttpResponseRedirect(reverse('profile'))