from django.shortcuts import render , HttpResponse
from django.views import View
from .models import Post

# Create your views here.

class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {'posts': posts}
        return render(request, 'base.html', context)