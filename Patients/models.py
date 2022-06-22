from django.db import models
from Accounts.models import Account

# Create your models here.
class Patient(models.model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    social = models.CharField(max_length=11)
    dob = models.DateField()
    account = models.ForeignKey(Account, blank = True, null = True, on_delete=models.CASCADEA)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"