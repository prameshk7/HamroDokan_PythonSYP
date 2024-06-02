from django import forms
from .models import profilemodel,productmodel,ordermodel
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profilemodel
        fields = ['address','phone','image']
   
class productupdateform(forms.ModelForm):   #product is just vendor
    class Meta:
        model = productmodel
        fields = ['name', 'location','whatsapp_number', 'description', 'imageshop']
        

class orderform(forms.ModelForm):
    class Meta:
        model = ordermodel
        fields = ['productmodel','nameofquantity','orderquantity']