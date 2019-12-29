from django.shortcuts import render
from .models import Post, Tag
# Create your views here.

def Main(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    return render(request, 'mainPage/main.html', context={'posts': posts, 'tags': tags})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    tags = Tag.objects.all()
    return render(request, 'mainPage/post_detail.html', context={'post': post, 'tags': tags})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'mainPage/tags_list.html', context={'tags': tags})

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    tags = Tag.objects.all()
    return render(request, 'mainPage/tag_detail.html', context={'tag': tag, 'tags': tags})