from django.http.response import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.db.models import F, Count
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import PermissionRequiredMixin

class HomeView(ListView):
    model = Post
    template_name = 'core/index.html'
    context_object_name = 'elem'
    #posts = Post.objects.aggregate(Count('id'))
    #print(posts)

    #def get_object(self, queryset=None):
    #    elements = Post.objects.order_by('-count_views')[:3]
    #    posts = Post.objects.aggregate(Count('id'))
    #    elements.users = Post.objects.aggregate(Count('id', distinct=True))
    #    print(posts)
    #    return elements
        #return super().get_object(queryset)
    
    def get_queryset(self):
        elements = Post.objects.order_by('-count_views')[:3]
        elements.posts = Post.objects.aggregate(Count('id'))
        elements.users = Post.objects.aggregate(Count('id', distinct=True))
        return super().get_queryset()
    
    
    #def get_popular(objects_number=3):
    #    elements = Post.objects.order_by('-count_views')[:objects_number]
    #    print(type(elements))
    #    return {'elements': elements}
    


class PostsView(PermissionRequiredMixin, ListView):
    model = Post
    raise_exception = False
    login_url = 'home'
    permission_required = 'core.view_post'
    paginate_by = 3
    template_name = 'core/posts.html'
    context_object_name = 'posts'
    ordering = ('-created_at',)
    redirect_field_name = 'next'    
   
    def get_queryset(self):
        posts_queryset = super().get_queryset().select_related('user')
        for post in posts_queryset:          
            post.likes = post.like_set.filter(status=True).count()
            post.dislikes = post.like_set.filter(status=False).count()
        return posts_queryset


class ViewPost(PermissionRequiredMixin, DetailView):
    model = Post
    login_url = 'home'
    permission_required = 'core.view_post'
    template_name = 'core/view_post.html'
    context_object_name = 'views'
    redirect_field_name = 'next'

    def get_object(self, queryset=None):
        view = Post.objects.get(pk=self.kwargs.get('pk'))
        view.count_views = F('count_views') + 1
        view.save()
        view.refresh_from_db()
        view.likes = view.like_set.filter(status=True).count()
        view.dislikes = view.like_set.filter(status=False).count()
        view.post_count = Post.objects.filter(user_id=view.user.pk).count()
        return view


class DeletePost(PermissionRequiredMixin, DeleteView):
    model = Post
    login_url = 'home'
    permission_required = 'core.view_post'
    template_name = 'core/delete_post.html'
    context_object_name = 'delete'
    success_url = reverse_lazy('all_posts')
    redirect_field_name = 'next'

    def get_object(self, queryset=None):
        owner = Post.objects.get(pk=self.kwargs.get('pk'))
        if owner.user != self.request.user:
            raise Http404('Not this time, body!')
        return super().get_object(queryset)

 

class CreatePost(PermissionRequiredMixin, CreateView):
    model = Post
    login_url = 'home'
    permission_required = 'core.view_post'
    form_class = PostForm
    template_name = 'core/create_post.html'
    redirect_field_name = 'next'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdatePost(PermissionRequiredMixin, UpdateView):
    model = Post
    login_url = 'home'
    permission_required = 'core.view_post'
    form_class = PostForm
    template_name = 'core/update_post.html'
    redirect_field_name = 'next'

    def get_object(self, queryset=None):
        owner = Post.objects.get(pk=self.kwargs.get('pk'))
        if owner.user != self.request.user:
            raise Http404('Not this time, body!')
        return super().get_object(queryset)
        