from django.db import models
from django.urls import reverse


class Blog(models.Model):
    post_date = models.DateField()
    author = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    description = models.TextField(
        max_length=1000, help_text="Enter the description of this blog.")


class Blogger(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(
        max_length=1000, help_text="Enter the bio of this blogger.")
