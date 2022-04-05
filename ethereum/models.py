from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.

class EthBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eth_balance = models.DecimalField(decimal_places=7, max_digits=19, default=0.0000017, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    
