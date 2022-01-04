from django.contrib import admin
from django.db.models.base import Model
from .models import Like, Post


class LikeAdmin(admin.TabularInline):
    model = Like



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'updated_at')
    ordering = ('created_at',)
    inlines = [LikeAdmin,]
