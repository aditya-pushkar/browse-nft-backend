from enum import unique
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

# class Tag(models.Model):
#     name = models.CharField(max_length=150, blank=True, null=True)

#     def save(self, *args, **kwargs):
#         name_case = self.name
#         if name_case.islower() != True: 
#             self.name = name_case.casefold()
#         super().save(*args, **kwargs)
    
#     def __str__(self):
#         return self.name


class Nft(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=500, blank=True)
    title = models.CharField(max_length=100, unique=True)
    img = models.URLField(max_length=2000)
    eth_price = models.DecimalField(max_digits=9, decimal_places=3, null=True, blank=True, default=00.000) # Price should be in eth
    redirect_link = models.URLField(max_length=2000) # This is the redirect link of nft webiste 
    tag1 = models.CharField(max_length=20, null=True, blank=True)
    tag2 = models.CharField(max_length=20, null=True, blank=True)
    tag3 = models.CharField(max_length=20, null=True, blank=True)
    tag4 = models.CharField(max_length=20, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def save(self, *args, **kwargs):
        username = self.user.username
        self.username = username    

        tag1 = self.tag1
        tag2 = self.tag2
        tag3 = self.tag3
        tag4 = self.tag4
        
        if tag1 != None:
            self.tag1 = tag1.casefold()
        if tag2 != None :
            self.tag2 = tag2.casefold()
        if tag3 != None:
            self.tag3 = tag3.casefold()
        if tag4 != None:
            self.tag4 = tag4.casefold()
        
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']

