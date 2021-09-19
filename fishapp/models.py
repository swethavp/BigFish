from django.db import models
from django.db.models.deletion import CASCADE
from bigfishapp.models import productdb


# Create your models here.
class contactdb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Email=models.CharField(max_length=30,null=True,blank=True)
    Subject=models.CharField(max_length=50,null=True,blank=True)
    Message=models.CharField(max_length=50,null=True,blank=True)

class registerdb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Email=models.CharField(max_length=30,null=True,blank=True)
    Address=models.CharField(max_length=50,null=True,blank=True)
    PhoneNo=models.IntegerField(null=True,blank=True)
    Username=models.CharField(max_length=20,null=True,blank=True)
    Password=models.CharField(max_length=20,null=True,blank=True)

class Cart(models.Model):
    productid=models.ForeignKey(productdb,on_delete=CASCADE,null=True,blank=True)
    userid=models.ForeignKey(registerdb,on_delete=CASCADE,null=True,blank=True)
    Username=models.CharField(max_length=10,null=True,blank=True)
    Total=models.IntegerField(null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    status = models.IntegerField(null=True,blank=True)
    Image=models.ImageField(upload_to='productimage/',blank=False,null=True)

class order(models.Model):
    cartid=models.ForeignKey(Cart,on_delete=CASCADE,null=True,blank=True)
    firstname=models.CharField(max_length=20,null=True,blank=True)
    lastname=models.CharField(max_length=20,null=True,blank=True)
    district=models.CharField(max_length=20,null=True,blank=True)
    street_address=models.CharField(max_length=30,null=True,blank=True)
    appartment=models.CharField(max_length=20,null=True,blank=True)
    town=models.CharField(max_length=20,null=True,blank=True)
    pin=models.IntegerField(null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    email=models.CharField(max_length=20,null=True,blank=True)


    
 
