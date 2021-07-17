from django.views import generic
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Post
from .forms import BlogForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


def add_post(request):
    """ View for store owner to add post """
    
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('add_post'))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_post(request, slug):
    """ Edit a blog post  """
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited blog post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to edit blog post. Please ensure the form is valid.')

    else:
        form = BlogForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def delete_post(request, slug):
    """ Delete a post from the blog """
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))
