from django.db import models

# Create your models here.

class Client(models.Model):
    CID = models.CharField(max_length = 12)
    Name = models.CharField(max_length = 50)
    Email = models.EmailField()
    Portfolio_ID = models.CharField(max_length = 15)
    PAN = models.CharField(max_length = 14)
    data_created = models.DateTimeField(auto_now_add = True)

class Broker(models.Model):
    BID = models.CharField(max_length = 12)
    Name = models.CharField(max_length = 50)
    Email = models.EmailField(null = True)
    License = models.CharField(max_length = 14)
    data_created  = models.DateTimeField(auto_now_add = True)

class Stock(models.Model):
    SID = models.CharField(max_length=12)
    Name = models.CharField(max_length = 50)
    Price = models.FloatField()
    Company = models.CharField(max_length=50)
    data_created = models.DateTimeField(auto_now_add=True)

class Client_Stock(models.Model):
    CID = models.ForeignKey(Client, on_delete = models.CASCADE)
    SID = models.ForeignKey(Stock, on_delete = models.CASCADE)
    Shares = models.FloatField()
    data_created = models.DateTimeField(auto_now_add=True)

class Client_Broker(models.Model):
    PID = models.ForeignKey(Client, on_delete = models.CASCADE)
    BID = models.ForeignKey(Broker, on_delete = models.CASCADE)
    data_created = models.DateTimeField(auto_now_add=True)