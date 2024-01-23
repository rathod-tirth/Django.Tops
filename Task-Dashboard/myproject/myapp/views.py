from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
   # for table
   user=User.objects.all()
   return render(request, "myapp/index.html", {'user':user})

def userForm(request):
   # form title
   title="Create"
   
   if request.POST:
      name=request.POST.get('name')
      
      # filtering out none values from the list
      rawSubject=[request.POST.get("python"),
               request.POST.get("django"),
               request.POST.get("js"),
               request.POST.get("react"),
               request.POST.get("flutter"),]
      subject=", ".join(list(filter(lambda i: i is not None, rawSubject)))
      gender=request.POST.get('gender')
      
      print("========>>>> Name :",name)
      print("========>>>> Subjects :",subject)
      print("========>>>> Gender :",gender)
      
      # checking for empty fields
      if name and subject and gender:
         # creating new user
         user=User.objects.create(name=name,subject=subject,gender=gender)
         print("========>>>> User :",user)
         msg="User Created Successfully"
         return render(request, 'myapp/userForm.html', {"msg":msg,"title":title})
      else:
         # error msg for empty fields
         l_msg="Please fill all the required fields before submitting the form."
         return render(request, 'myapp/userForm.html', {'l_msg':l_msg,"title":title})
   
   # default render
   return render(request, 'myapp/userForm.html',{"title":title})

def editUser(request,k):
   # form title
   title="Edit"
   msg=None
   
   user=User.objects.get(id=k)
   
   if user:
      if request.POST:
         user.name=request.POST.get('name') or user.name
         # filtering out none values from the list
         rawSubject=[request.POST.get("python"),
               request.POST.get("django"),
               request.POST.get("js"),
               request.POST.get("react"),
               request.POST.get("flutter"),]
         subject=", ".join(list(filter(lambda i: i is not None, rawSubject)))
         
         user.subject=subject or user.subject
         user.gender=request.POST.get('gender') or user.gender
         user.save() # updating the user
         msg="User Edit Successfully"
      
      print("==========>>> Name :",user.name)
      print("==========>>> Subject :",user.subject)
      print("===========>>>> Gender ;",user.gender)
      context={'e_user':user,
               'title':title,
               'msg':msg}
      
      return render(request, 'myapp/userForm.html', context)

def deleteUser(request,k):
   user=User.objects.get(id=k)
   user.delete() # deleting the user
   return redirect('home')