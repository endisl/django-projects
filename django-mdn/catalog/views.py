from django.shortcuts import get_object_or_404, render
from django.views import generic
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
