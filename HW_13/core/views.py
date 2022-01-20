from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from .models import Post


class PostsView(ListView):
    model = Post
    template_name = 'core/posts.html'
    context_object_name = 'posts'
    ordering = ('-updated_at',)

   
    def get_queryset(self):
        posts_queryset = super().get_queryset().select_related('user')
        for post in posts_queryset:          
            post.likes = post.like_set.filter(status=True).count()
            post.dislikes = post.like_set.filter(status=False).count()
            post.count = Post.objects.filter(user_id=post.user.pk).count()
        return posts_queryset


class ViewPost(DetailView):
    model = Post
    template_name = 'core/view_post.html'
    context_object_name = 'views'

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        view = Post.objects.get(pk=pk)
        view.likes = view.like_set.filter(status=True).count()
        view.dislikes = view.like_set.filter(status=False).count()
        view.post_count = Post.objects.filter(user_id=view.user.pk).count()
        return view


class DeletePost(DeleteView):
    model = Post
    template_name = 'core/delete_post.html'
    context_object_name = 'delete'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('all_posts')
