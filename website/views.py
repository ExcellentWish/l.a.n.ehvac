from django.shortcuts import render
from django.conf import settings
from django.views import View
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.views.decorators.csrf import csrf_protect

# Create your views here.

@csrf_protect
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            customer_name = form.cleaned_data['name']
            email_from = form.cleaned_data['email']
            subject = (f'Questions from {customer_name}, from website, email: {email_from}')
            message = form.cleaned_data['message']
            recipient_list = [settings.EMAIL_HOST_USER]
            cd = form.cleaned_data

            # Send an email using the send_mail() function
            send_mail(subject, message, email_from, recipient_list)
        # Set submitted to True to display success message
            submitted = True
            messages.add_message(
                request, messages.SUCCESS,
                "Thank you for contacting us, one of our staff will be in "
                "touch shortly.")

        else:
            form = ContactForm()
            submitted = False

    return render(request, 'index.html', {'form': form, 'submitted': submitted})


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
