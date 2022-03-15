from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    docType = models.IntegerField(null=False)
    docNumber = models.BigIntegerField(null=False)
    role = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=256)

class BankTeller(models.Model):
    name = models.CharField(max_length=50)
    
class Service(models.Model):
    service_id = models.BigAutoField(primary_key=True)
    serviceName = models.CharField(max_length=50)
    description = models.TextField()
    serviceType = models.IntegerField()
    teller_id = models.ForeignKey(BankTeller, on_delete=models.CASCADE,null=True)

class Ticket(models.Model):
    orderNumber = models.CharField(max_length=50)
    userId = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    serviceId = models.ForeignKey(Service, on_delete=models.CASCADE,null=True)
    state = models.IntegerField()
    arrivalDate = models.DateField(auto_now_add=True)
    arrivalTime = models.TimeField(auto_now_add=True)


