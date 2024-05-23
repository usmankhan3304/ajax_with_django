from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import *
class UserRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    username = forms.CharField(label="Username", max_length=255, required=False)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    re_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        re_password = cleaned_data.get('re_password')

        if password1 and re_password and password1 != re_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
        )
        user.first_name = self.cleaned_data['name']
        user.save()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=255)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)



class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields=['title','description']
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        print(self.user)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance