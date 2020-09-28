from django import forms

class Login(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class Signup(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    pic = forms.ImageField()

class Contact(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(max_length=100)