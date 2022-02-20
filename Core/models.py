from django.db import models

# Create your models here.


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    docType = models.CharField(max_length=50,null=False)
    docNumber = models.CharField(max_length=50,null=False)
    role = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=50)

class Service(models.Model):
    service_id = models.BigAutoField(primary_key=True)
    serviceName = models.CharField(max_length=50)
    description = models.TextField()
    serviceType = models.IntegerField()

class BankTeller(models.Model):
    name = models.CharField(max_length=50)
    orderId = models.ForeignKey(Service, on_delete=models.CASCADE)

class Ticket(models.Model):
    orderNumber = models.IntegerField()
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
    serviceId = models.ForeignKey(Service,on_delete=models.CASCADE)
    state = models.IntegerField()
    arrivalDate = models.DateField()
    arrivalTime = models.TimeField()


