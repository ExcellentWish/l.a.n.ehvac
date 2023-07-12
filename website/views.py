from django.shortcuts import render
from django.conf import settings
from django.views import View
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            # Send an email using the send_mail() function
            send_mail(
                'Question Form Submission',
                f'Name: {cd["name"]}\nEmail: {cd["email"]}\nMessage: {cd["message"]}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            # Set submitted to True to display success message
            submitted = True
    else:
        form = ContactForm()
        submitted = False

    return render(request, 'base.html', {'form': form, 'submitted': submitted})


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
