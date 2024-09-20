from django.db import models

class data(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=25)
    number = models.IntegerField(max_length=10)
    message = models.CharField(max_length=50)
