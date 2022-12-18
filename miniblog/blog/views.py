import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import CreateCommentForm
from .models import Blog, Blogger, Comment


def index(request: HttpRequest):
    """View function for home page of site."""

    num_blogs = Blog.objects.all().count()

    context = {
        'num_blogs': num_blogs,
    }

    return render(request, 'index.html', context=context)


class BlogListView(ListView):
    model = Blog
    paginate_by = 5


class BlogDetailView(DetailView):
    model = Blog


class BloggerListView(ListView):
    model = Blogger
    paginate_by = 5


class BloggerDetailView(DetailView):
    model = Blogger


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['description', ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'], })
