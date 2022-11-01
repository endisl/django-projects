from django.http import HttpRequest
from django.shortcuts import render
from django.views import generic
from .models import Author, Book, BookInstance, Genre


def index(request: HttpRequest):
    """View function for home page of site."""

    num_books = Book.objects.all().count()

    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    num_authors = Author.objects.count()

    num_books_vent = Book.objects.filter(title__icontains='vent').count()

    num_genres_fiction = Genre.objects.filter(
        name__icontains='fiction').count()

    num_visits = request.session.get('num_vists', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_books_vent': num_books_vent,
        'num_genres_fiction': num_genres_fiction,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='war')[:5]

    # def get_context_data(self, **kwargs):
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     context['some_data'] = 'Some data'
    #     return context


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author
