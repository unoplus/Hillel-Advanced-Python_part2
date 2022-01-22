from django.urls import path
from .views import PostsView, ViewPost, DeletePost


urlpatterns = [
    path('', PostsView.as_view(), name='all_posts'),
    path("post/<int:pk>/", ViewPost.as_view(), name="post_view"),
    path("delete_post/<int:pk>/", DeletePost.as_view(), name="delete"),
]

