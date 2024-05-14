from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from Notes_app.forms import UserRegistrationForm
def index(request):
    return render(request,'notes/index.html')

"""Signup page goes here..."""

def signup(request): 
    form=UserRegistrationForm()
    return render(request,'notes/signup.html',{'form':form})