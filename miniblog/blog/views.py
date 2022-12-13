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


class BloggerDetailView(DetailView):
    model = Blogger


@login_required
@permission_required('catalog.can_create_comment', raise_exception=True)
def create_comment(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('blog-detail'))
    else:
        form = CreateCommentForm()

    context = {
        'form': form,
        'blog': blog
    }

    return render(request, 'blog/blog_create_comment.html', context)


# class CommentCreate(CreateView):
#    model = Comment
#    fields = ['author', 'post_date', 'description']
#    permission_required = 'blog.can_create_comment'
