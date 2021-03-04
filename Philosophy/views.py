
from django.shortcuts import render



# Home page request

def home(request):
    return render(request, 'fontend/home.html')