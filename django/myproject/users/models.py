from django.db import models

# Create your models here.
class AddUser(models.Model):
    username = models.CharField(max_length=100,unique=True)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,primary_key=True)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirmpassword = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='static/image')




def __str__(self):
    return f'{self.username}'

