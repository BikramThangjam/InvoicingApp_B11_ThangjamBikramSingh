from django.db import models

# Create your models here.

class Invoice(models.Model):
    invoice_id = models.IntegerField()
    client_name = models.CharField(max_length=200)
    date = models.DateField()

class Item(models.Model):
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE, null=True,blank=True, related_name="items")
    description = models.TextField()
    rate = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    
class User(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=20)
    
