
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from .models import Profile
import datetime
 

class SignUpForm(forms.ModelForm):

    username = forms.CharField(label='Username', max_length=30,widget=forms.TextInput(attrs={'required': True,'placeholder':'User Name','name':'username'}))
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'required': True,'placeholder':'Email Address'}))

    password1= forms.CharField(label='Password',
                          widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password (Again)',
                        widget=forms.PasswordInput())
    first_name=forms.CharField(label='First Name')
    last_name=forms.CharField(label='Last Name')

    class Meta:
        model = Profile
        fields = ('username','first_name','last_name','email', 'password1', 'password2','Interest','Genre','Associated_with')

    

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']

class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['Post', 'File']
        
