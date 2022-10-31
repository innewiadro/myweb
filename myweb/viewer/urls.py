from django.urls import path
from .views import index, PostList, PostDetail, about_me, PostUpdateView, PostDeleteView, PostCreateView

urlpatterns =[
    path("", PostList.as_view(), name="index"),
    path("posts/", PostList.as_view(), name="posts"),
    path('posts/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('posts/new', PostCreateView.as_view(), name="post-create"),
    path('posts/<slug:slug>/edit', PostUpdateView.as_view(), name='post-update'),
    path('posts/<slug:slug>/delete', PostDeleteView.as_view(), name='post-delete'),
    path("about_me", about_me, name="about_me"),
]