from django.db import models
class Product(models.Model):
    name=models.CharField(max_length=20)
    dob=models.DateField()
    email=models.EmailField()
    phno=models.IntegerField()
