from django.db import models

# Create your models here.

class Member(models.Model):
    FullName=models.CharField(max_length=200)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=50)
    Email=models.EmailField(max_length=100,unique=True) 
    
    MobileNo=models.IntegerField(unique=True)
    Address=models.CharField(max_length=500)
    Batch=models.CharField(max_length=200)
    JoiningDate=models.DateField()

    def __str__(self):
        return self.FullName

class Payment(models.Model):
    PaymentId=models.IntegerField(unique=True)
    MemberId=models.IntegerField()
    PaymentAmount=models.FloatField()
    PaymentMethod=models.CharField(max_length=20)
    PaymentDate=models.DateField()
    Status=models.CharField(max_length=20) 
    def __str__(self): 
        return 'Payments'

class Batch(models.Model):
    MemberId=models.IntegerField()
    BatchTiming=models.DateTimeField()

    def __str__(self):
        return 'Batch' 




