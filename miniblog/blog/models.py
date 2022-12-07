from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    post_date = models.DateField()
    description = models.TextField(
        max_length=1000, help_text="Enter the description of this blog.")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-detail", args=[str(self.id)])

    class Meta:
        ordering = ['post_date']


class Blogger(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(
        max_length=1000, help_text="Enter the bio of this blogger.")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blogger-detail", args=[str(self.id)])


class Comment(models.Model):
    author = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    post_date = models.DateField()
    description = models.TextField(
        max_length=1000, help_text="Enter comment about blog here.")
    blog = models.ForeignKey(
        Blog, on_delete=models.SET_NULL, null=True)
    blogger = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['post_date']
