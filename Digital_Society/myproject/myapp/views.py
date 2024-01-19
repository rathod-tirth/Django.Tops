from django.shortcuts import render,redirect
from django.urls import reverse
from .models import *
import random
from .utils import *

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
   # to prevent non-logged in access to the profile
   if 'email' in request.session:
      context=data(request.session['email'])
      return render(request, 'myapp/profile.html', context)
   else:
      return redirect('login')

def update_pass(request):
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

def update_profile(request):
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
         chairman.pic=request.FILES.get("pic") or chairman.pic
         chairman.save()
   
   return redirect(reverse('profile'))

def addMember(request):
   if 'email' in request.session:
      context=data(request.session['email'])
      
      if request.POST:
         # --------- password -----------
         email=request.POST.get('email')
         contact=request.POST.get('contact')
         li=["fds32","1as3df","98dsf6","asdf132","l4y6h3","j45gf","k4hg65"]
         password=random.choice(li)+email[3:8]+contact[5:9]
         print("==========>>>> Password",password)
         # ------------------------------
         
         user=User.objects.create(email=email, password=password, role="Member")
         print("===========>>> User",user)
         if user:
            member=Member.objects.create(userid=user,
                                         firstname=request.POST.get('firstname'),
                                         lastname=request.POST.get('lastname'),
                                         contact=request.POST.get('contact'),
                                         blockno=request.POST.get('blockno'),
                                         houseno=request.POST.get('houseno'),
                                         occupation=request.POST.get('occupation'),
                                         vehicleno=request.POST.get('vehicleno'),
                                         tenant=request.POST.get('tenant'),
                                         familyno=request.POST.get('familyno'),
                                         )
            
            print("===========>>> Member",member)
            print("===========>>> Firstname",member.firstname)
            context['msg']="Member Added Successfully"
            
            if member:
               print("=============>>> Sending Mail")
               sendmail("Digital Society One Time Password","mailtemplate",email,{'email':email,'password':password,'firstname':member.firstname})
      
      return render(request, 'myapp/addMember.html', context)
   else:
      return redirect('login')
   
def allMember(request):
   if 'email' in request.session:
      context=data(request.session['email'])
      mall=Member.objects.all()
      context['mall']=mall
      
      return render(request, 'myapp/allMember.html',context)
   else:
      return redirect('login')
   
def editMember(request,pk):
   if 'email' in request.session:
      context=data(request.session['email'])
      member=Member.objects.get(id=pk)
      context['member']=member
      
      if request.POST:
         member.firstname=request.POST.get('firstname') or member.firstname
         member.lastname=request.POST.get('lastname')  or member.lastname
         member.contact=request.POST.get('contact') or member.contact
         member.blockno=request.POST.get('blockno') or member.blockno
         member.houseno=request.POST.get('houseno') or member.houseno
         member.occupation=request.POST.get('occupation') or member.occupation
         member.tenant=request.POST.get('tenant') or member.tenant
         member.familyno=request.POST.get('familyno') or member.familyno
         member.vehicleno=request.POST.get('vehicleno') or member.vehicleno
         member.pic=request.FILES.get("pic") or member.pic
         member.save()
         return redirect('allMember')
         
      return render(request, 'myapp/editMember.html',context)
   else:
      return redirect('login')
   
def deleteMember(request,pk):
   if 'email' in request.session:
      member=Member.objects.get(id=pk)
      member.delete()
      
      return redirect('allMember')
   else:
      return redirect('login')
   
def addNotice(request):
   if 'email' in request.session:
      context=data(request.session['email'])
      
      if request.POST:
         notice=Notice.objects.create(title=request.POST.get('title'),
                                      description=request.POST.get('description'),
                                      pic=request.POST.get('pic'),
                                      video=request.POST.get('video'),)
         print("===========>>> Notice",notice.title)
         context['msg']="Notice Added Successfully"

      return render(request, 'myapp/addNotice.html',context)
   else:
      return redirect('login')
   
def allNotice(request):
   if 'email' in request.session:
      context=data(request.session['email'])
      notice=Notice.objects.all()
      context['notice']=notice

      return render(request, 'myapp/allNotice.html',context)
   else:
      return redirect('login')