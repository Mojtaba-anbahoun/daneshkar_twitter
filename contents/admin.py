from django.contrib import admin
from .models import Post, Tag , Image, Comment, Category
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'category' , 'body']
    search_fields = ['category', 'user']
    list_filter = ['category', 'user']


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


#@admin.register(Reaction)
#class ReactionAdmin(admin.ModelAdmin):
#    list_display = ['id', 'user', 'post']
#    search_fields = ['user', 'post']
#    list_filter = ['user', 'post']



