from pyexpat import model
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from requests import request

# Create your models here.
class pages(models.Model):
    name = models.CharField(max_length=100)
    tobic = models.TextField(max_length=5000)
    
    def __str__(self) -> str:
        return self.name
