from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Note
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        validate_password(password1, self.instance)
        return password1


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "category", "content", "image", "video", "voice"]

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get("category")
        image = cleaned_data.get("image")
        video = cleaned_data.get("video")
        voice = cleaned_data.get("voice")
