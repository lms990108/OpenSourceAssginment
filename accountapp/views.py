from django.http import HttpResponse
from django.shortcuts import render

from .models import Post
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'accountapp/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'accountapp/post_detail.html', {'post': post})
