import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import RenewBookForm
from .models import Author, Book, BookInstance, Genre


class BlogListView():
    pass


class BloggerListView():
    pass


class BlogDetailView():
    pass


class BloggerDetailView():
    pass


class BlogCreate():
    pass
