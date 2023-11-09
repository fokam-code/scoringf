from django.urls import path
from .views import login_blog
urlpatterns = [
    path('login',login_blog,name='login-blog')
    
]
