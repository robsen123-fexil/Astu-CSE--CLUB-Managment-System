from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=10000000)
    date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.title
from django.db import models


class info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length = 10,default = "M")


class Application(models.Model):
    email = models.EmailField()
    programming_preference = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.email 
# models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    attendance = models.IntegerField(default=0)
    report = models.TextField(blank=True)
    contest_score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    