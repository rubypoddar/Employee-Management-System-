from django.db import models

class AddEmployee(models.Model):

    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    PassWord = models.CharField(max_length=100)
    