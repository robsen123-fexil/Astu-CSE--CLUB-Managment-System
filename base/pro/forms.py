
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

        # Remove common password check
        # (Note: Removing this check weakens password security)
        # if password1.lower() in self.common_passwords:
        #     raise ValidationError(self.error_messages['password_too_common'])

        # Custom password validation checks
        if len(password1) < 4:
            raise ValidationError("Password must be at least 4 characters.")
        if password1.isdigit():
            raise ValidationError("PASSWORD MUST CONTAIN LETTER AND DIGIT.")
        # Add more custom checks as needed

        return password1
