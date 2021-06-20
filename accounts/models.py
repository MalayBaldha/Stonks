from django.db import models

# Create your models here.

class Client(models.Model):
    ID = models.CharField(max_length=12)
    Name = models.CharField(max_length = 50)
    Email = models.CharField(max_length=50)
    Portfolio_Id = models.IntegerField(max_length=14)
    PAN = models.CharField(max_length=14)
    data_created = models.DataTimeField(auto_now_add=True)

class Broker(models.Model):
    ID = models.CharField(max_length=12)
    Name = models.CharField(max_length = 50)
    Email = models.CharField(max_length=50)
    License_No = models.CharField(max_length=14)
    data_created = models.DataTimeField(auto_now_add=True)

class Stocks(models.Model):
    ID = models.CharField(max_length=12)
    Name = models.CharField(max_length = 50)
    Price = models.IntegerField(max_length=20)
    Company = models.CharField(max_length=50)
    data_created = models.DataTimeField(auto_now_add=True)

class Client_Stocks(models.Model):
    Client_id = models.CharField(max_length=12)
    Stock_ID = models.CharField(max_length=12)
    