from django.db import models


# Create your models here.
class admindb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Email=models.CharField(max_length=50,null=True,blank=True)
    Password=models.CharField(max_length=20,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    FileUpload=models.ImageField(upload_to='adminimage/',blank=False,null=True)

class categorydb(models.Model):
    Category_name=models.CharField(max_length=30,null=True,blank=True)
    Category_description=models.CharField(max_length=100,null=True,blank=True)
    FileUpload=models.ImageField(upload_to='categoryimage/',blank=False,null=True)

class productdb(models.Model):
    Product_Name=models.CharField(max_length=30,null=True,blank=True)
    Product_Weight=models.CharField(max_length=30,null=True,blank=True)
    Product_Price=models.CharField(max_length=30,null=True,blank=True)
    Product_Category=models.CharField(max_length=30,null=True,blank=True)
    Image=models.ImageField(upload_to='productimage/',blank=False,null=True)

class recipedb(models.Model):
    Recipe_Name=models.CharField(max_length=30,null=True,blank=True)
    Recipe_Ingredients=models.CharField(max_length=100,null=True,blank=True)
    Recipe_Instructions=models.CharField(max_length=100,null=True,blank=True)
    Recipe_Image=models.ImageField(upload_to='recipeimage/',blank=False,null=True)

