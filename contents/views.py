from django.shortcuts import redirect, render
from contents.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def post(request):
    if request.method == "GET":
        return render(request, "post.html")
    elif request.method == "POST":
        my_post = Post()
        my_post.title = request.POST.get("title")
        my_post.content = request.POST.get("content")
        my_post.update_at = request.POST.get("update_at")
        my_post.save()
        return redirect("/")

def postdelete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/')


def postupdate(request, id): 
    if request.method == "GET":
        post = Post.objects.get(id=id)
        return render(request, 'update.html', {"post":post})

    if request.method == "POST":
        post = Post.objects.get(id=id)
        post.title = request.POST.get('title', '')
        post.content = request.POST.get('content', '')
        post.save()

        
        return redirect('/', id)
    