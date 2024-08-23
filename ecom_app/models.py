from django.db import models
from django.contrib.auth.models import User,AbstractUser,Group,Permission
# Create your models here.
import secrets


class Account(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
    contact=models.CharField(max_length=254)
    profile=models.ImageField(upload_to="")
    

class Product(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to="")
    price=models.IntegerField()

class Addshopping(models.Model):
    product_id=models.IntegerField() 
    user_id=models.IntegerField()







