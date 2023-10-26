from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post,Comment
from django.shortcuts import get_object_or_404
from accounts.models import UserProfile

# Create your views here.
def index(request):
    return render(request,'blog/index.html',{})

def post(request,slug):
    post=get_object_or_404(Post,slug=slug)
    if request.method =="GET":
        return render(request,'blog/post.html',{'post':post})
    elif request.method =="POST":
        body=request.POST.get('body')
        comment=Comment(
            body=body,
            author=UserProfile.objects.last(),
            post=post,
        )
        comment.save()
        return render(request,'blog/post.html',{'post':post})

def posts(request):
    blog_post= Post.objects.all().order_by("-created_at")[:10]
    return render(request,'blog/posts.html',{'blog_post':blog_post})
