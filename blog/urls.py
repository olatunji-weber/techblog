from django.urls import path
from .views import CommentListCreate, PostDetail, PostListCreate, post_list, post_detail

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('api/posts/', PostListCreate.as_view(), name='post_list_create'),
    path('api/posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('api/comments', CommentListCreate.as_view(), name='comment_list_create'),
]