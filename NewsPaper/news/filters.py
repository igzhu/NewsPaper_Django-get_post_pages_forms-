from django_filters import FilterSet, DateTimeFromToRangeFilter, CharFilter
from django.db import models
from .models import Post, Author

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
           'postDatetime': ['gt'],
           'head': ['icontains'],
           'postAuthor__authorName__username': ['icontains'],
       }
