from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog-home.html', context)

def blog_single(request,pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,pk=pid)
    single = Post.objects.get(pk=pid)
    nextpost = Post.objects.filter(id__gt=single.id).order_by('id').first()
    prevpost = Post.objects.filter(id__lt=single.id).order_by('id').last()
    context = {
        'posts': posts,
        'post': post,
        'nextpost': nextpost,
        'prevpost': prevpost,
        'single':single
    }
    return render(request, 'blog/blog-single.html', context)











