from django.contrib import admin
from .models import Post
from .models import register
admin.site.register(Post)
admin.site.register(register)