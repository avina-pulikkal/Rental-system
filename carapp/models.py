from django.db import models

# Create your models here.


class registermodel(models.Model):
    firstname=models.CharField(max_length=200,null=True)
    middlename=models.CharField(max_length=200,null=True)
    lastname=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    gender=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    psw=models.CharField(max_length=200,null=True)

class bookingmodel(models.Model):
    name=models.CharField(max_length=200,null=True)
    vehiclename=models.CharField(max_length=200,null=True)
    price=models.CharField(max_length=200,null=True)
    booking=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    # disease=models.CharField(max_length=200,null=True)
