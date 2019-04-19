from django.db import models

# Create your models here.
class AKHBAR(models.Model):
    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    text = models.TextField()
    time = models.TimeField(auto_now=False)
    def summary(self):
        return self.text[:100]
    def __str__(self):
        return self.title