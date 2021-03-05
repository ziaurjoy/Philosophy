
from django.shortcuts import render

from blog.models import BlogPost, Category

# Home page request

def home(request):
    categoris = Category.objects.all()
    posts = BlogPost.objects.all()
    context = {
        'categoris': categoris,
        'posts': posts
    }
    return render(request, 'fontend/home.html', context)


