from django.urls import path
from .views import PostsView, UpdatePost, ViewPost, DeletePost, CreatePost


urlpatterns = [
    path('', PostsView.as_view(), name='all_posts'),
    path("post/<int:pk>/", ViewPost.as_view(), name="post_view"),
    path("delete_post/<int:pk>/", DeletePost.as_view(), name="delete_post"),
    path("create_post/", CreatePost.as_view(), name="create_post"),
    path("update_post/<int:pk>/", UpdatePost.as_view(), name="update_post"),
]

