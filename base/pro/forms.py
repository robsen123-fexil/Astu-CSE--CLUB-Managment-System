
from django import forms
from .models import Post
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password', 'email', 'username']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError

class CustomPasswordChangeForm(PasswordChangeForm):
    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')
        if len(password1) < 4:
            raise ValidationError("Password must be at least 4 characters.")
        if password1.isdigit():
            raise ValidationError("PASSWORD MUST CONTAIN LETTER AND DIGIT.")
        

        return password1

class DeletePostForm(forms.Form):
    selected_posts = forms.ModelMultipleChoiceField(
        queryset=Post.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

from django import forms
from .models import Application

class YourForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['email', 'programming_preference', 'year', 'description']