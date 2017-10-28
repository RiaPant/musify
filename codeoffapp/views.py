from django.shortcuts import render
from django.db import models
from django import template
from django.contrib.auth.models import User
from django.template.loader import get_template
from codeoffapp.form import SignUpForm
from codeoffapp.models import Profile
from django.conf import settings

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import smtplib
from django.db import models
from django import template
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import redirect

from django.http import JsonResponse
from django.core import serializers
from django.core.mail import send_mail, BadHeaderError
import pprint
import datetime
import json
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def login_user(request):
    if request.method == "POST":
        mail = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=mail, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                request.session['id'] = user.id

                return render(request, 'codeoffapp/home.html')
            else:
                return HttpResponse("Inactive User")
        else:
            return render(request, 'codeoffapp/login.html',{'error_message':"Invalid user Credentials"})
    return render(request, 'codeoffapp/login.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        print ("Hello!")

       # if form.is_valid():
        username = request.POST.get('username')
        email =request.POST.get('email')
        password = request.POST.get('password1')
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        Interest=request.POST.get('Interest')
        Genre=request.POST.get('Genre')
        Associated_with=request.POST.get('Associated_with')
        print ("Hello!")

        p1=User(username=username,email=email,password=password,first_name=firstname,last_name=lastname)
        p1.set_password(password)
        p1.save()
        newUser=Profile(user=p1,Interest=Interest,Genre=Genre,Associated_with=Associated_with)
        newUser.save()
        print ("Hello!1")
        subject = 'Registration Successful- Musify'

        message = 'Greetings! You have been successfully registered on Musify - An Online Music Platform. Now you can easily find friends anywhere by just visiting our website. '
        from_email = 'shareadcare@gmail.com'
        email_msg="Subject: {} \n\n{}".format(subject,message)
        smtp = smtplib.SMTP('smtp.gmail.com',587)
        smtp.starttls()
        smtp.login('shareadcare@gmail.com','mirsajsob2017')
        smtp.sendmail('shareadcare@gmail.com',email,email_msg)
        smtp.quit()
        
        return render(request, 'codeoffapp/login.html')
    #else:
        print ("Hello!ERROE")

        form = SignUpForm()
        context={
        'form':form,
        'error_message':"Invalid User details"
        }
        return render(request, 'codeoffapp/register.html',context)

    form = SignUpForm()
    return render(request, 'codeoffapp/register.html',{'form': form})

def view_profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.session['id'])
        userprofile = Profile.objects.get(user=user)
        context = {
        'userprofile':userprofile,
                }
        return render(request, 'codeoffapp/view_profile.html', context)
    else:
        return render(request, 'codeoffapp/login.html')

def home(request):
    return render(request, 'codeoffapp/home.html')


