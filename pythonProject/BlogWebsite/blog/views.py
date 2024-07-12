from django.shortcuts import render
from .models import Post, Comment, Category
from django.contrib.auth.models import User

def main(request):
    return render(request, 'main.html')

def users(request):
    users_list = User.objects.all()
    return render(request, 'users.html', {'users_list': users_list})

def blogs(request):
    posts = Post.objects.all()
    return render(request, 'blogs.html', {'posts': posts})

def blog_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blogdetails.html', {'post': post})

def comments(request):
    comments_list = Comment.objects.all()
    return render(request, 'comments.html', {'comments_list': comments_list})

def categories(request):
    categories_list = Category.objects.all()
    return render(request, 'categories.html', {'categories_list': categories_list})
