from django.db import models

# Create your models here.
class Account(models.model):
    name = models.CharField(max_length=32)
    