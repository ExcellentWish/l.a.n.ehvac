from django.shortcuts import render
from django.conf import settings
from django.views import View
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.

def index(request):
    # Return homepage
    return render(request, 'base.html')

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            assert False
            return HttpResponseRedirect('base.html')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'base.html', {'form':form, 'submitted':submitted})

def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
