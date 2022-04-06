from django.db import models
from User.models import *
from datetime import date

class Categories(models.Model):
    category = models.CharField(max_length=30)

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    category =models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Coupons(models.Model):
    coupen_name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    percent = models.IntegerField()
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    used = models.BooleanField(default=False)
    live = models.BooleanField(default=False)

    @property
    def is_started(self):
        return date.today() >= self.start


    @property
    def is_valid(self):
        return date.today() > self.end

class Offer(models.Model):
    category = models.OneToOneField(Categories,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    discount = models.DecimalField(max_digits=20,decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    start = models.BooleanField(default=False)

    @property
    def is_valid(self):
        return date.today() > self.end_date
    
    @property
    def is_started(self):
        return date.today() >= self.start_date
