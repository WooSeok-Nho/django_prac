from django.urls import path
from . import views

app_name='contents'
urlpatterns = [
    path("post/", views.post,name="post"),
    path("postdelete/<int:id>", views.postdelete, name="postdelete"),
    path("postupdate/<int:id>", views.postupdate, name="postupdate"),

 ]