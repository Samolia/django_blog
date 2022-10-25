from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name='my_posts'),
    path('post/<int:pk>/', views.post_details, name='post_details'),
    path('post/new/', views.post_new, name='new_post'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_drafts_list, name='post_drafts_list'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
]
