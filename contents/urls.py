from django.urls import path
from . import views

app_name='contents'
urlpatterns = [
    path("post/", views.post,name="post"),
    path("postdelete/<int:id>", views.postdelete, name="postdelete"),
    path("postupdate/<int:id>", views.postupdate, name="postupdate"),
    path('comment/<int:id>',views.write_comment, name='write_comment'),
    path('comment/delete/<int:id>',views.comment_delete, name='comment_delete'),
    path("like/<int:id>", views.like,name="like"),


 ]