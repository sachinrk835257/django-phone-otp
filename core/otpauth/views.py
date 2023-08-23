from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from otpauth.models import Custumer
import random
import uuid
from otpauth import phone_otp


# Create your views here.

def signup(request):
    title = '''sign up page'''
    if request.method == "POST":

        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            messages.add_message(request, messages.WARNING,
                                 "PASSWORD NOT MATCH !!")
            return redirect('/auth/signup/')

        if (Custumer.objects.filter(custumer_phone_number=phone_number).exists() or User.objects.filter(username=email).exists()):
            messages.add_message(request, messages.WARNING,
                                 "PHONE NUMBER EXIST !")
            return redirect('/auth/signup/')
        user_obj = User.objects.create_user(email=email, username=email)
        user_obj.set_password(pass2)
        user_obj.save()

        print("rgfgnfggcn\n")
        # custumer_obj = Custumer.objects.filter(custumer_phone_number=phone_number)
        # custumer_obj = Custumer.objects.get(user = user_obj)
        token = str(uuid.uuid4())
        custumer_obj = Custumer.objects.create(user = user_obj, custumer_phone_number = phone_number, phone_otp = str(random.randint(1000, 9999)), uuid = token)
        # custumer_obj.custumer_phone_number = phone_number
        # custumer_obj.phone_otp = random.randint(1000, 9999)
        # custumer_obj.uuid = str(uuid.uuid4())
        custumer_obj.save()

        phone_otp_verify(uuid,phone_otp)
        return redirect(f'/auth/otp/{token}/')

        # messages.add_message(request, messages.WARNING, f"{e}")
        # return redirect('/auth/signup/')

    return render(request, 'auth/signup.html', {"title": title})


def phone_otp_verify(request):
    title = '''otp verification'''
    '''one time phone otp verification is done here'''
    return render(request, 'auth/otp.html', {"title": title})


def logout_page(request):
    title = '''login page'''
    return render(request, 'auth/login.html', {"title": title})
