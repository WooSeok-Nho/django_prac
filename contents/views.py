from django.shortcuts import redirect, render
from contents.models import Post,Comment
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
        my_post.user = request.user

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


def write_comment(request, id):
    if request.method == 'GET':
        return render(request, "comment.html",id)
    elif request.method == 'POST':
        current_comment = Post.objects.get(id=id)
        content = request.POST.get('content')
        if content=='':
            return redirect('/')


        my_comment = Comment()
        my_comment.content = content
        my_comment.user = request.user
        my_comment.post = current_comment
        my_comment.save()

    return redirect('/')
    
def comment_delete(request, id):
    comment = Comment.objects.get(id=id)
    if request.user == comment.user:
        comment.delete()
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(request.META['HTTP_REFERER'])
        

@login_required
def like(request, id):
    me = request.user
    click_post = Post.objects.get(id=id)
    if me in click_post.like_authors.all():
        click_post.like_authors.remove(request.user)
    else:
        click_post.like_authors.add(request.user)
    return redirect(request.META['HTTP_REFERER'])   


