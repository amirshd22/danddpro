from django.db import models

# Create your models here.
class AKHBAR(models.Model):
    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=850)
    time = models.TimeField(auto_now=False)