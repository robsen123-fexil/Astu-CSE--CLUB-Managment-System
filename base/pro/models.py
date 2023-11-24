from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=10000000)
    date = models.DateTimeField(default=datetime.now, blank=True, editable=False)

class register(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)


# models.py


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    year = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name
