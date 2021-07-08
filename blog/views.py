from django.shortcuts import render
from .models import Post


def blog(request):
    queryset = Post.objects.filter(status=1).order_by('-created_on')

    return render(request, 'blog/blog.html')


def post_detail(request):
    model = Post

    return render(request, 'blog/post_detail.html')
