from operator import mod
from turtle import title
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date= models.DateTimeField('date published')