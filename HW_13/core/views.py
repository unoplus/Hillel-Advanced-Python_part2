from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.db.models import F
from .models import Post
from .forms import PostForm


class PostsView(ListView):
    paginate_by = 3
    model = Post
    template_name = 'core/posts.html'
    context_object_name = 'posts'
    ordering = ('-created_at',)
    
   
    def get_queryset(self):
        posts_queryset = super().get_queryset().select_related('user')
        for post in posts_queryset:          
            post.likes = post.like_set.filter(status=True).count()
            post.dislikes = post.like_set.filter(status=False).count()
        return posts_queryset


class ViewPost(DetailView):
    model = Post
    template_name = 'core/view_post.html'
    context_object_name = 'views'

    def get_object(self, queryset=None):
        view = Post.objects.get(pk=self.kwargs.get('pk'))
        view.count_views = F('count_views') + 1
        view.save()
        view.refresh_from_db()
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
 

class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'core/create_post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdatePost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'core/update_post.html'
    pk_url_kwarg = 'pk'