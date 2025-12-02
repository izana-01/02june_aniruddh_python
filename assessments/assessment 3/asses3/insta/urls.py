from django.urls import path
from . import views

app_name = 'insta'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/<int:id>/like/', views.like_post, name='like_post'),
    path('user/<int:user_id>/follow/', views.toggle_follow, name='toggle_follow'),
    path('create/', views.create_post, name='create_post'),
    
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
]
