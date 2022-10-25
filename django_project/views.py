from django.http import HttpResponse
from django.shortcuts import render, redirect
from users.models import User
from django.contrib.auth import authenticate, login as loginsession


def home(request):
    user = request.user.is_authenticated
    if user:
        users = User.objects.all()
        context = {
            "users":users
        }
        return render(request, 'home.html', context)

    else:
        return render(request, 'login.html')


