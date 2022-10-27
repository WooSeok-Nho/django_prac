from . import views
from django.urls import path

app_name= 'users'


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('delete/', views.delete, name ='delete'),
    path('update/<int:id>/', views.update, name ='update'),
    path('user_follow/<int:id>', views.user_follow, name='user_follow'),
    path('follow_view/', views.follow_view, name='follow_view'),

    

]

