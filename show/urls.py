from django.urls import path,re_path
from . import views
from django.contrib.auth import login
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('index/',views.index,name='index'),
    path('movie_detail/<int:pk>/',views.mdetail,name='movie_detail') ,
    path('movie_detail/<int:pk>/',views.like,name='like'),
    path('tl/<int:pk>/',views.theatre_list,name='tl'),
    path('signup/',views.Signup.as_view(),name = 'signup'),
    path('',auth_view.LoginView.as_view(template_name="login.html" ,success_url="{%url 'index' %}"),name='login'),
    path('book/<int:pk>/',views.show_details.as_view(),name='book-t'),
    re_path(r'^book-ticket/(?P<pk>\d+)/',views.bookticket,name="book-ticket"),
    path('pay/',views.pay,name='pay'),
    path('confirm/',views.confirm,name='confirm'),
    path('profile/',views.profile,name='profile'),
    path('rate/',views.rate,name='rate'),
    
]