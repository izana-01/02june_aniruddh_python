from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# DRF router for API endpoints
router = DefaultRouter()
router.register(r'api/users', views.UserViewSet)
router.register(r'api/profiles', views.ProfileViewSet)
router.register(r'api/posts', views.PostViewSet)
router.register(r'api/comments', views.CommentViewSet)

urlpatterns = [
    # Template views
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('post/create/', views.post_create_view, name='create_post'),
    path('post/<int:pk>/', views.post_detail_view, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit_view, name='edit_post'),
    path('post/<int:pk>/delete/', views.post_delete_view, name='delete_post'),
    path('post/<int:pk>/like/', views.toggle_like_view, name='like_post'),  

    # API views
    path('', include(router.urls)),
]
