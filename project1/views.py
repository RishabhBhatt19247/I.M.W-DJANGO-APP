from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def first(request): 
    return render(request,'1.html')
def second(request):
    return render(request,'2.html')    
def doctors(request): 
    return render(request,'doctors.html')
def help(request): 
    return render(request,'help.html')
def hospitals(request): 
    return render(request,'hospitals.html')
def registerform(request): 
    return render(request,'registerform.html')
def handlesignup(request):
    if request.method=='POST': 
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.error(request,"❌ This email is allready signed,kindly try with another email")
            return redirect('first')
        elif User.objects.filter(username=username,password=password).exists():  
            messages.error(request,"❌ This username is allready signed,kindly try with another username")
            return redirect('first')   
        else:    
            myuser=User.objects.create_user(username,email,password)       
            myuser.save()
            messages.success(request,"✅ You have successfully signin")
            return redirect('second')
    else:
        return HttpResponse('error 404 - not found')  
        
def handlelogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"✅ You have successfully login")
            return redirect('second')
        else:
            messages.error(request,"❌ Wrong Credentials")
            return redirect('first')
           
    else:
        return HttpResponse('error 404- not found')     
              
def handlelogout(request):
    logout(request) 
    messages.success(request,"✅ You have successfully logout")      
    return redirect('first')     







