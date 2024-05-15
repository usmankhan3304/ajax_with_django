from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from Notes_app.forms import UserRegistrationForm
def index(request):
    return render(request,'notes/index.html')

"""Signup page goes here..."""

from django.http import JsonResponse

def signup(request): 
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # You can include any additional data you want in the JSON response
            response_data = {'status': 'success', 'message': 'User registered successfully'}
            return JsonResponse(response_data)
    else:
        form = UserRegistrationForm()
    return render(request, 'notes/signup.html', {'form': form})

def success_page(request):
    return render(request, 'notes/success.html')