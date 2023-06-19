from django.contrib import admin
from .models import Post, Tag , Image, Comment, Category , Reaction
# Register your models here.


class PostImageInline(admin.TabularInline):
    model = Image
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'category' , 'body']
    search_fields = ['category', 'user']
    list_filter = ['category', 'user']
    inlines = [PostImageInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    search_fields = ['text']
    list_filter = ['posts']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'alt', 'image', 'post']
    search_fields = ['name']
    list_filter = ['post']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'user', 'post', 'reply_to']
    search_fields = ['user']
    list_filter = ['post']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post_field']
    search_fields = ['user', 'post_field']
    list_filter = ['user', 'post_field']



