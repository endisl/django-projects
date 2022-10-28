from django.shortcuts import HttpResponse, render
from .models import Author, Book, BookInstance, Genre


def index(request):
    """View function for home page of site."""

    num_books = Book.objects.all().count()

    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    num_authors = Author.objects.count()

    num_books_vent = Book.objects.filter(title__icontains='vent').count()

    num_genres_fiction = Genre.objects.filter(
        name__icontains='fiction').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_books_vent': num_books_vent,
        'num_genres_fiction': num_genres_fiction
    }

    return render(request, 'index.html', context=context)
