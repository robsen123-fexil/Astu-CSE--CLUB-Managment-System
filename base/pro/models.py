from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=10000000)
    date = models.DateTimeField(default=datetime.now, blank=True, editable=False)
