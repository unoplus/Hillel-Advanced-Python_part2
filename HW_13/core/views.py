from django.views.generic import ListView
from .models import Post


class PostsView(ListView):
    model = Post
    template_name = 'core/posts.html'
    context_object_name = 'posts'
    ordering = ('-updated_at',)

    def get_queryset(self):
        posts_queryset = super().get_queryset()
        for post in posts_queryset:
            post.likes = post.like_set.filter(status=True).count()
            post.dislikes = post.like_set.filter(status=False).count()
            post.count = Post.objects.filter(user_id=post.user.pk).count()
           
        return posts_queryset   
