from django.db import models

# Create your models here.
class book(models.Model):
    bname=models.CharField(max_length=50)
    aname=models.CharField(max_length=50)
    bdesc=models.TextField()
    bprice=models.IntegerField()

# name of object
    def __str__(self):
        return self.bname

# Form Model
class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.email
