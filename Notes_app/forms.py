from django import forms


class UserRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    re_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)