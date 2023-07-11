from django.shortcuts import render
from django.conf import settings
from django.views import View
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.

def index(request):
    # Return homepage
    return render(request, 'base.html')


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
