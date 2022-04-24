from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('login/',Login,name='login'),
    path('signup/',Signup_view.as_view(),name='signup'),
    path('profile/',profile.as_view(),name='profile'),
    path('logout/', log_out, name='logout'),
    path('',welcom,name='welcome'),
    path('profile-setting/',profile_stteing.as_view(),name='profile-setting'),
    path('post/',great_post.as_view(),name='post'),
    path('user/<str:username>/',friend_profile.as_view(),name='friend-profile'),
    path('search',searchview.as_view(),name='search'),
    path('follwo/<int:id>/',friend_follwo,name='friend-follwo'),
    path('unfollwo/<int:id>/',friend_unfollwo,name='friend-unfollwo'),
    path('home/',HomePage.as_view(),name='home')

]