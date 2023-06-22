from django import forms
from django.contrib.auth.models import User


class ShareNoteForm(forms.Form):
    shared_with = forms.ModelChoiceField(
        queryset=User.objects.all(), empty_label="Select a user"
    )
