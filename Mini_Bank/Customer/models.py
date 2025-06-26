
# Create your models here.
from django.db import models
from django.utils import timezone

class Transaction(models.Model):
    From_account = models.CharField(max_length=20)
    To_account = models.CharField(max_length=20)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Timestamp = models.DateTimeField(default=timezone.now)
    Remarks = models.TextField(blank=True, null=True)
