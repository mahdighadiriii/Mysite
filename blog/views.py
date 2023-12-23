from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1).order_by('-published_date')
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

@login_required
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
    return render (request,'blog/blog-single.html',context)

@login_required
def blog_search(request):
    #print(request.__dict__)
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        #print(request.GET.get('s'))
        # if s := request.GET.get('s'): #use this method only when your using python version 3.8 and above
        if request.GET.get('s'):
            s =  request.GET.get('s')
            posts = posts.filter(content__contains=s)
    
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)





