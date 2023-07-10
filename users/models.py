from django.db import models
from datetime import date
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100,blank=False, )
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(default=date.today)
    country = models.CharField(max_length= 30)
    email = models.EmailField(unique=True)
    password= models.CharField(max_length=100, blank=False, null=False)


    def __str__(self):
        return self.name

    