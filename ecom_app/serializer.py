from rest_framework import serializers
from .models import *
from django.contrib.auth.forms import UserCreationForm
class   AccountSerializers(UserCreationForm):
    
    class Meta:
        model=Account
        fields="__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=Product
        fields="__all__"  

class AddshoppingSerializer(serializers.ModelSerializer):

    class Meta:
        model=Addshopping
        fields="__all__"
        
        