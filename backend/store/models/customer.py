from email.headerregistry import Address
from pyexpat import model
from django.db import  models
from django.contrib.auth.models import User    

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    mobileNumber = models.IntegerField(null=True, blank=True)
    alternateMobileNumber = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    Address = models.CharField(max_length=100, null=True, blank=True)
    

