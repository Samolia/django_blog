from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name='my_posts'),
    path('post/<int:pk>/', views.post_details, name='post_details'),
]
