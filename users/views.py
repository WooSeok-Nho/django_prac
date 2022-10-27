import profile
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login as loginsession
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password


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

@login_required
def logout(request):
        auth.logout(request)
        return redirect('users:login')

@login_required
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        logout(request)
    return render(request, 'login.html')


def update(request ,id):
    if request.method == "GET":
        return render(request, 'profile.html')
    elif request.method == "POST":
        user = User.objects.get(id=id)
        user.email = request.POST.get("email")
        user.username = request.POST.get("username")
        user.nickname = request.POST.get("nickname")
        origin_password = request.POST["origin_password"]
        check = check_password(origin_password, user.password)
        if check:
            new_password = request.POST["new_password"]
            user.set_password(new_password)
            user.save()
            return redirect("/")
@login_required
def user_follow(request, id):
    me = request.user
    click_user = User.objects.get(id=id)
    if me in click_user.followee.all():
        click_user.followee.remove(request.user)
    else:
        click_user.followee.add(request.user)
    return redirect(request.META['HTTP_REFERER'])   
    


@login_required
def follow_view(request): #
    if request.method == 'GET':
        user_list = User.objects.all().exclude(email=request.user.email)
        return render(request, 'follow.html',{"user_list":user_list})




    

