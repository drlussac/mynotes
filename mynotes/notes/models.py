from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Note(models.Model):
    CATEGORY_CHOICES = (
        ("simple", "Simple Note"),
        ("image", "Image Note"),
        ("video", "Video Note"),
        ("voice", "Voice Note"),
    )

    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    video = models.FileField(upload_to="videos/", null=True, blank=True)
    voice = models.FileField(upload_to="voices/", null=True, blank=True)
    content = models.TextField(default="")

    def __str__(self):
        return self.title


def clean(self):
    if self.category.name != "simple":
        if not self.image and not self.video and not self.voice:
            raise ValidationError(
                "At least one of the image, video, or voice fields is required."
            )
