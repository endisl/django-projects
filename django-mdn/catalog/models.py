from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL)
    summary = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass


class BookInstance(models.Model):
    pass


class Author(models.Model):
    pass
