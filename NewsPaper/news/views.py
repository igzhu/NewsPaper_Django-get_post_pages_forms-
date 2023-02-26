from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from .models import Post
from .filters import PostFilter

# Create your views here.


class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-postDatetime')
    paginate_by = 10


class PostDetails(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostSearch(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-postDatetime')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context
