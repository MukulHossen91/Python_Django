from django.db import models

# Create your models here.

class laptop(models.Model):
    mobile = models.CharField(max_length=50)
    re_mobile = models.CharField(max_length=50)
    laptop = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=50)
    about = models.CharField(max_length=100)
    textarea = models.CharField(max_length=250)
    checkbox = models.BooleanField(max_length=50)
    ram = models.IntegerField()
    ssd = models.CharField(max_length=50)
    youtube_chanel = models.BooleanField(max_length=50)


