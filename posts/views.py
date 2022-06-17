from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Post, Comment
from .forms import NewPostForm, NewCommentForm
from .helpers import *

from django.http import HttpResponse

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-id')
    # comments_total = 0
    # for post in posts:
        # comments_total

    if request.method == "POST":
        try:
            form = NewPostForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                user_name = form.cleaned_data['user_name']
                author_email = form.cleaned_data['email']
                content = form.cleaned_data['content']
                image = form.cleaned_data['image']
                post = Post(
                    title=title,
                    user_name=user_name,
                    author_email=author_email,
                    content=content,
                    image=image
                )
                post.save()
                return HttpResponseRedirect(reverse('post-thread', args=[post.slug]))
            else:
                print('Form is invalid')
        except Exception as exc:
            print(exc)
            return HttpResponseRedirect(reverse('main'))
    else:
        form = NewPostForm()

    return render(request, 'posts/index.html', {
        'posts': posts,
        'form': form,
        # 'comments_total': comments_total
    })

def post_thread(request, post_slug, comment_slug=None):
    post = Post.objects.get(slug=post_slug)
    form = NewCommentForm()
    comments = Comment.objects.filter(to_post=post.id)
    reply_to_comment = comments.get(slug=comment_slug) if comment_slug else None

    if request.method == "POST":
        try:
            form = NewCommentForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                user_name = form.cleaned_data['user_name']
                user_email = form.cleaned_data['email']
                content = form.cleaned_data['content']
                image = form.cleaned_data['image']
                comment = Comment(
                    title=title,
                    user_name=user_name,
                    user_email=user_email,
                    content=content,
                    image=image,
                    to_post=post,
                    to_comment=reply_to_comment
                )
                comment.save()
                return HttpResponseRedirect(reverse('post-thread', args=[post.slug]))
            else:
                print('Form is invalid')
        except Exception as exc:
            print(exc)
            return HttpResponseRedirect(reverse('post-thread', args=[post.slug]))

    return render(request, 'posts/post-thread.html', {
        'post': post,
        'form': form,
        'comments': comments,
        'comments_tree': comments_tree(comments),
        'reply_to_comment': reply_to_comment
    })
