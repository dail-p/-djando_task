from django.shortcuts import render
from django.views.generic import ListView

from posts.models import Post

class PostsListView(ListView):
    queryset = Post.objects.filter(status="published")
    context_object_name = "posts"
    template = "posts/post_list.html"
