from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from Admin.models import *

class User(AbstractUser):
    profile_picture = models.ImageField(upload_to = 'pics', null = True)
    phone = models.BigIntegerField(null = True)
    district = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    whats_app_no = models.CharField(max_length=15, null=True, blank=True)
    def __str__(self, ):
        return str(self.name)

    class meta:
        db_table = "User"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cart_product = models.ForeignKey(Product, on_delete = models.CASCADE, null = True)  
    quantity = models.IntegerField(null=True, blank=True)

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    totalprice = models.IntegerField(null=True, blank=True)
    tid = models.CharField(max_length=200, null=True, blank=True)
    tdate = models.DateField(null=True, blank=True)
    payment_status = models.CharField(max_length=50, null=True, blank=True)
    order_status = models.CharField(max_length=50, null=True, blank=True)
    payment_mode = models.CharField(max_length=50, null=True, blank=True)