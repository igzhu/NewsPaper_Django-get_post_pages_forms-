#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.


class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-postDatetime')


class PostDetails(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'