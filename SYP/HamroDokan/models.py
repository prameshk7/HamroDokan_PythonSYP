from django.db import models
from django.contrib.auth.models import User


# This is the model for identifying the user profiles
class userprofilemodel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_vendor = models.BooleanField(default=False)

    # Add any other profile fields you need

    def __str__(self):
        return self.user.username
    
    


# This is the vendor listing page where vendor themself list their shop name, location and description
class productmodel(models.Model):
    name= models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    whatsapp_number = models.CharField(max_length=20,default='')  # Store WhatsApp number as string
    description=models.CharField(max_length=1000)
    imageshop = models.ImageField(default='',upload_to='vendor_images')
    
    
    def __str__(self):
        return f'{self.name} {self.location}'
    
    class Meta:
        verbose_name_plural = 'Shop List'
# models.py

# productmodel is kinda vendor listings
# staffmodel should be removed or needs to be user model

# below is what a user orders from their make purchase section
class ordermodel(models.Model):
    productmodel= models.ForeignKey(productmodel,on_delete=models.CASCADE,null=True)
    nameofquantity= models.CharField(max_length=100,null=True)
    staffmodel = models.ForeignKey(User,models.CASCADE,null=True)
    orderquantity = models.PositiveIntegerField(null=True)
    dates = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.productmodel} ordered by {self.staffmodel}'
    
    class Meta:
        verbose_name_plural = 'Orders'
        
class profilemodel(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(default='',upload_to='Profile_images')
    
    def __str__(self):
        return f'{self.staff.username}-profilemodel'
    