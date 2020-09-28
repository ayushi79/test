from django import forms

class Review(forms.Form):
    name = forms.CharField(max_length=50)
    message = forms.CharField(max_length=150)  
class Signup(forms.Form):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    dob = forms.DateField(widget=forms.SelectDateWidget)
    gender = forms.CharField(max_length=50)
    hobby = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=12)
    password = forms.CharField(widget=forms.PasswordInput)
    confirmpassword = forms.CharField(widget=forms.PasswordInput)

    pic = forms.ImageField()

class Login(forms.Form):
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)




