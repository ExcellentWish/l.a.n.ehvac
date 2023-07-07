from django.shortcuts import render
from django.conf import settings
from django.views import View

# Create your views here.


# Create your views here.

def index(request):
    # Return homepage
    return render(request, 'base.html')