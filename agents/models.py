from django.db import models
from datetime import datetime

# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    address = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    landline = models.CharField(max_length=20, blank=True)

    facebook = models.CharField(max_length=200, blank=True)
    twitter = models.CharField(max_length=200, blank=True)
    google = models.CharField(max_length=200, blank=True)
    linkedin = models.CharField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    is_mvp = models.BooleanField(default=False)
    join_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name