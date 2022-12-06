import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import RenewBookForm
from .models import Blog, Blogger


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


class BookListView(ListView):
    model = Book
    paginate_by = 10

    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='war')[:5]

    # def get_context_data(self, **kwargs):
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     context['some_data'] = 'Some data'
    #     return context


class BookDetailView(DetailView):
    model = Book


class AuthorListView(ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(DetailView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    "Generic class-based view listing books on loan to current user"
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class LoanedAllBooksListView(PermissionRequiredMixin, ListView):
    "Generic class-based view listing all books on loan"
    model = BookInstance
    template_name = 'catalog/bookinstance_list_all_borrowed.html'
    paginate_by = 10
    permission_required = 'catalog.can_mark_returned'

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    book_instance = get_object_or_404(BookInstance, pk=pk)

    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            return HttpResponseRedirect(reverse('all-borrowed'))
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance
    }

    return render(request, 'catalog/book_renew_librarian.html', context)


class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    intial = {'date_of_death': '21/10/2021'}
    permission_required = 'catalog.can_mark_returned'


class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'summary', 'isbn', 'genre', 'language']


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')
