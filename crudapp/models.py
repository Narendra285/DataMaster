from django.db import models

class studentdata(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    mobile=models.IntegerField()
    marks1=models.IntegerField()
    marks2=models.IntegerField()
    marks3=models.IntegerField()
    marks4=models.IntegerField()
    marks5=models.IntegerField()

# Create your models here.
