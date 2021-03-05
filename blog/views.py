from django.shortcuts import render
from .models import *
# Create your views here.


def post_details(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'fontend/postdetails.html',context)