from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    post_date = models.DateField(default=date.today)
    description = models.TextField(
        max_length=2000, help_text="Enter your blog text here.")

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-detail", args=[str(self.id)])


class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(
        max_length=500, help_text="Enter your bio here.")

    class Meta:
        ordering = ['user', 'bio']

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("blogger-detail", args=[str(self.id)])


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_date = models.DateField(auto_now_add=True)
    description = models.TextField(
        max_length=1000, help_text="Enter comment about blog here.")
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return self.description
