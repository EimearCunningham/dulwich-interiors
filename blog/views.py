from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import BlogForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def add_post(request):
    """ Add a post to the blog """
    form = BlogForm()
    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
