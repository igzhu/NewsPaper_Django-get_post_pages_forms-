from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator

from .models import Post, Category, User
from .filters import PostFilter
from .forms import PostForm
# Create your views here.


class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    form_class = PostForm
    queryset = Post.objects.order_by('-postDatetime')
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save
        return super().get(request, *args, **kwargs)


class PostDetails(DetailView):
    template_name = 'news/post_detail.html'
    queryset = Post.objects.all()


class PostSearch(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'posts'
    #form_class = PostForm
    #form_class = PostFilter
    queryset = Post.objects.order_by('-postDatetime')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = User.objects.all()
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostAdd(CreateView):
    template_name = 'news/post_add.html'
    #context_object_name = 'posts'
    form_class = PostForm

class PostEdit(UpdateView):
    template_name = 'news/post_add.html'
    form_class = PostForm
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class PostDelete(DeleteView):
    template_name = 'news/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'
