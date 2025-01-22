from django.contrib import admin


from .models import Hashtag, Post, Comment, Reaction, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'bio', 'pic')
    list_display_links = ('id', 'username', 'email')
    search_fields = ('id', 'username', 'email')
    list_filter = ('username', 'email')
    ordering = ('username', 'email')
    fields = ('username', 'email', 'bio', 'pic')


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name',)
    list_filter = ('name', 'created_at')
    ordering = ('name', 'created_at')
    fields = ('name', 'created_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'content', 'created_at', 'updated_at')
    list_display_links = ('id', 'author', 'content')
    search_fields = ('id', 'author', 'content')
    list_filter = ('author', 'created_at', 'updated_at')
    ordering = ('-created_at', '-updated_at')
    fields = ('author', 'content', 'hashtags', 'created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'content', 'created_at')
    list_display_links = ('id', 'user', 'post', 'content')
    search_fields = ('id', 'user', 'post', 'content')
    list_filter = ('user', 'post', 'created_at')
    ordering = ('-created_at',)
    fields = ('user', 'post', 'content', 'parent_comment', 'created_at')


@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'comment', 'type', 'created_at')
    list_display_links = ('id', 'user', 'post', 'comment', 'type')
    search_fields = ('id', 'user', 'post', 'comment', 'type')
    list_filter = ('user', 'post', 'comment', 'type', 'created_at')
    ordering = ('-created_at',)
    fields = ('user', 'post', 'comment', 'type', 'created_at')


