from re import search
from django.contrib import admin
from .models import Like, Post


class LikeAdmin(admin.TabularInline):
    model = Like

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'updated_at')
    search_fields = ('title', )
    list_filter = ('user', 'updated_at')
    ordering = ('-updated_at',)
    inlines = [
        LikeAdmin,
    ]


admin.site.register(Post, PostAdmin)
