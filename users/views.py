from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login as loginsession
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        passwordcheck = request.POST.get('passwordcheck')
        nickname = request.POST.get('nickname')
        if password == passwordcheck:
            User.objects.create_user(email=email, password=password, nickname=nickname, username=username)
            return render(request, 'login.html')
        else:

            return HttpResponse("비밀번호가 틀렸습니다.")
    
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email , password=password)
        if user is not None:
            loginsession(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error':'이메일 인증 or 이메일 패스워드를 확인해 주세요!'})


def logout(request):
        auth.logout(request)
        return redirect('users:login')

def delete(request):
        user = request.user
        user.delete()
        logout(request)
        return render(request, 'login.html')

@login_required
def userupdate(request):
    if request.method == 'GET':
        return render(request, 'profile.html')
    elif request.method == 'POST':
        user = request.user

        email = request.POST.get('email')
        username = request.POST.get('username')
        new_user_pw = request.POST.get('new_user_pw')

        user.email = email
        user.first_name = username
        user.set_password(new_user_pw)

        user.save()


        return redirect('/')





    

