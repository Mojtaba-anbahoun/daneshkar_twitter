from django.urls import path
from .views import PostView
from . import views

urlpatterns = [
    path('', views.home),
    path('posts/', PostView.as_view(), name="show_posts"),
]

