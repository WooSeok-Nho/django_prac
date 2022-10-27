from django.http import HttpResponse
from django.shortcuts import render, redirect
from users.models import User
from django.contrib.auth import authenticate, login as loginsession
from contents.models import Post,Comment


def home(request):
        if request.method == 'GET':
            user = request.user.is_authenticated

        if user:
            post_all = Post.objects.all()
            posts = []
            for post in post_all:
                comment = Comment.objects.filter(post_id=post.id).order_by('created_at')
                post.comment = comment
                posts.append(post)

            return render(request, 'home.html',{"posts":posts})

        else:
            return render(request, 'login.html')
                


