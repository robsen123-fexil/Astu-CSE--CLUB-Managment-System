from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=10000000)
    date = models.DateTimeField(default=datetime.now, blank=True, editable=False)
    def __str__(self):
        return self.title
from django.db import models


class info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length = 10,default = "M")
