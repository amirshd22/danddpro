from django.db import models


class Kharid(models.Model):
    img = models.ImageField(upload_to="images/")
    price = models.CharField(max_length=55)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
