from django.db import models

# Create your models here.
class Prediction(models.Model):  #models is class and its variable is Model
    ppw=models.CharField(max_length=20)
    pn=models.CharField(max_length=20)
    mi = models.CharField(max_length=20)
    appm = models.CharField(max_length=20)
    result = models.CharField(max_length=50)
