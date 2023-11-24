
from django import forms
from .models import Post
from django import forms
from .models import Student
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'department', 'skills', 'email', 'phone_number', 'year']
