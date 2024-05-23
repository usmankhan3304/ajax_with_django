from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Notes
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from Notes_app.forms import UserRegistrationForm,NoteForm
from .forms import UserLoginForm

def index(request):
    if request.user.is_authenticated:
        form = NoteForm()
        if request.method == 'POST':
            form = NoteForm(request.POST, user=request.user)
            if form.is_valid():
                form.save()
                return JsonResponse({"message":"Note have saved successfully!"}) 
                 
                # Optionally, redirect to a success page or render the same page with a success message
             # Redirect to the same page to avoid resubmission issues
        return render(request, 'notes/index.html', {'form': form})
    else:
        return redirect('login')

# class NoteCreateView(LoginRequiredMixin, CreateView):
#     model = Notes
#     form_class = NoteForm
#     template_name = 'notes/index.html'
#     success_url = reverse_lazy('home')  # Adjust the success URL as needed

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

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
def user_login(request):
    # Redirect authenticated users to home
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                response_data = {'status': 'success', 'message': 'Login successful'}
            else:
                response_data = {'status': 'error', 'message': 'Invalid username or password'}
        else:
            response_data = {'status': 'error', 'message': 'Invalid credentials, username, or password'}
        
        return JsonResponse(response_data)
    else:
        form = UserLoginForm()
    
    return render(request, 'notes/login.html', {'form': form})
       
   
      

def success_page(request):
    return render(request, 'notes/success.html')
def logout_page(request):
   logout(request)
   return redirect('login')

