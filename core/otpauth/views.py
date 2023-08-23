from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from otpauth.models import Custumer



# Create your views here.

def signup(request):
    title = '''sign up page'''
    if request.method == "POST":
        try:

            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            pass1 = request.POST.get('pass1')
            pass2 = request.POST.get('pass2')
            User.objects.filter(username=email)
            if pass1!=pass2:
                messages.add_message(request, messages.WARNING, "PASSWORD NOT MATCH !!")
                return redirect('/auth/signup/')

            
            if (Custumer.objects.filter(custumer_phone_number = phone_number).exists() or User.objects.filter(username=email).exists()):
                messages.add_message(request, messages.WARNING, "PHONE NUMBER EXIST !")
                return redirect('/auth/signup/')
            user = User.objects.create_user(email=email,username=email)
            user.set_password(pass2)
            user.save()

            custumer_obj = Custumer.objects.filter(user = user)
            print(custumer_obj)
        except Exception as e:
            messages.add_message(request, messages.WARNING, f"{e}")
            return redirect('/auth/signup/')
        
        
        
         

    return render(request,'auth/signup.html',{"title":title})

def phone_otp_verify(request):
    title = '''otp verification'''
    '''one time phone otp verification is done here'''
    return render(request,'auth/otp.html',{"title":title})

def logout_page(request):
    title = '''login page'''
    return render(request,'auth/login.html',{"title":title})