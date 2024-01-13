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
      return render(request, 'myapp/profile.html', context)
   else:
      return redirect('login')

# function for changing the password
def change_pass(request):
   # getting the current and new password
   c_password=request.POST.get("c_password")
   n_password=request.POST.get("n_password")
   print("===============>>> ",c_password,n_password)
      
   # checking if the values are empty or not
   if c_password != None and c_password!="" and n_password != None and n_password!="":
      
      # User table / user object to access all the details of that particular user
      user=User.objects.get(email=request.session['email'])
      print("=========>>>> Password :",user.password)
      
      # password checking
      print("================>>>> Password checking")
      if user.password == c_password:
         # if correct then passord changed to new password
         user.password=n_password
         user.save()
         
         print("================>>>> Password Right")
         w_msg="Password Updated Successfully"
         # making user re-loggin with new password 
         del request.session['email']
         return render(request, 'myapp/login.html', {'w_msg':w_msg})
      else:
         # if incorrect then loggin-out user for safeaty reasons
         print("================>>>> Password Wrong")
         msg="Invalid Current Password"
         return render(request, 'myapp/login.html', {'msg':msg})
   
   return redirect(reverse('profile'))

def change_details(request):
   if 'email' in request.session:
      user=User.objects.get(email=request.session['email'])
      chairman=Chairman.objects.get(userid=user.id)
      print("================>>>",user, chairman)
      
      # updating the user details
      if request.POST:
         chairman.firstname=request.POST.get('firstname') or chairman.firstname
         chairman.lastname=request.POST.get('lastname')  or chairman.lastname
         chairman.contact=request.POST.get('contact') or chairman.contact
         chairman.blockno=request.POST.get('blockno') or chairman.blockno
         chairman.houseno=request.POST.get('houseno') or chairman.houseno
         if 'pic' in request.FILES:
            chairman.pic=request.FILES.get("pic")
         chairman.save()
   
   return redirect(reverse('profile'))