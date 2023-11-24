from django.db import models
from datetime import datetime



class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=10000000)
    date = models.DateTimeField(default=datetime.now, blank=True, editable=False)
    def __str__(self):
        return self.title
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100)
