from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class User(models.Model):  
    joined       = models.DateTimeField('date created', auto_now_add=True)  
    firstname    = models.CharField(max_length=30, blank=True)
    lastname     = models.CharField(max_length=30, blank=True)
    email        = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)

class Item(models.Model):
    
    region        = models.CharField(max_length=30, blank=True)    
    serial_number = models.CharField(max_length=30, blank=True)
    size          = models.CharField(max_length=30, blank=True)
    #status        = on-loan
    #gender        = [M, F, U]
    # pictures

class Transaction(models.Model):
    # user = models.ForeginKey
    # items = models.OneToMany
    # signed_out = models.DateTimeField('date created', auto_now_add=True)
    # due_back = models.DateTimeField('date created', auto_now_add=True)