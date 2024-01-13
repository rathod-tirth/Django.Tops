from django.shortcuts import render,redirect
from django.urls import reverse
from .models import *

# Create your views here.

# default url
def home(request):
   if 'email' in request.session:
      context=data(request.session['email'])   
      return render(request, 'myapp/index.html',context)
   
   return render(request, "myapp/login.html")

def login(request):
   # if the user is already logged-in
   if 'email' in request.session:
      context=data(request.session['email'])   
      return render(request, 'myapp/index.html',context)
   else:
      msg=None
      try:
         # getting user input from html
         print("=========>>> Login")
         user_email=request.POST.get('email')
         user_password=request.POST.get('password')
         print("=========>>>",user_email,user_password)
         
         if(user_email != None and user_password != None):
            # if the user input is correct get the user data as an object
            context=data(user_email,user_password)
            # creating a session, so the app have an info that the user is logged-in or not
            request.session['email']=context['user'].email
            
            # rendering the dashboard
            print("========== render index")
            return render(request, 'myapp/index.html',context)
         
      except Exception as e:
         print("===========>>> Error =",e)
         msg="Invalid Input Pls Enter Again"
         
      return render(request, "myapp/login.html", {'msg':msg})
   
def logout(request):
   print("==============>>> logout")
   if "email" in request.session:
      # deleting the session to notifi that the user is logged out
      del request.session['email']
   return redirect(reverse('login'))

# function for fetching user data
def data(f_email,f_password=None):
   # getting all the user data
   user_data=User.objects.get(email=f_email)
   if f_password:
      user_data=User.objects.get(email=f_email, password=f_password)
      
   chairman_data=Chairman.objects.get(userid=user_data.id)
   print("==============>>>",user_data,chairman_data)
   
   # creating a context for html
   context={
            "user":user_data,
            "chairman":chairman_data,
         }
   
   return context

def profile(request):
   context=None
   # to prevent non-logged in access to the profile
   if 'email' in request.session:
      context=data(request.session['email'])
      
      # getting the current and new password
      c_password=request.POST.get("c_password")
      n_password=request.POST.get("n_password")
      print("===============>>> ",c_password,n_password)
      
      # calling the change_pass function only when the password field are filled
      if c_password != None and c_password!="" and n_password != None and n_password!="":
         # the function returns a tuple msg and boolean vaule
         msg,result=change_pass(request,c_password,n_password)
         
         # based on boolean msg and page is rendered
         if result:
            context['msg']=msg
            return render(request, 'myapp/profile.html', context)
         else:
            # for safety reasons loggin out if the password is incorrect
            del request.session['email']
            return render(request, 'myapp/login.html', {'msg':msg})
         
      return render(request, 'myapp/profile.html', context)
   else:
      return redirect('login')

# function for changing the password
def change_pass(request,c_password,n_password):
   # User table / user object to access all the details of that particular user
   user=User.objects.get(email=request.session['email'])
   print("=========>>>> Password :",user.password)
   
   # password checking
   print("================>>>> Password checking")
   if user.password == c_password:
      # new password if correct
      user.password=n_password
      user.save()
      # alert for user
      print("================>>>> Password Right")
      msg="Password Updated Successfully"
      # returning msg and True for correct
      return msg,True
   else:
      # returning msg and False for incorrect
      print("================>>>> Password Wrong")
      msg="Invalid Current Password"
      return msg,False
