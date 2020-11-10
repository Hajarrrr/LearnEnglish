from django.db import models
#added soon
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=50)


# Create your models here.
