from django.http import HttpResponse
from django.shortcuts import render, redirect
from users.models import User
from django.contrib.auth import authenticate, login as loginsession
from contents.models import Post


def home(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            my_post = Post.objects.all()
            return render(request, 'home.html',{"posts":my_post})

        else:
            return render(request, 'login.html')
    


