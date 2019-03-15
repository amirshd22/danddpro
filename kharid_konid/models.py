from django.db import models

# Create your models here.
class Kharid(models.Model):
    img = models.ImageField(upload_to="images/")
    text = models.CharField(max_length =255)
    price = models.CharField(max_length=55)
    date =  models.DateField()